export interface Place {
  description_place: string;
  image: string;
  typical_food: string;
  languages: string;
  traditional_music: string;
  city_tourist_map: string;
  map_of_tourist_places_in_ecuador: string;
  hotels: string;
  regions: string;
  location: string;
  created_at: string;
}
import {
  RecomendacionesCards,
  CiudadInfo,
  GeoSearch,
} from "@/interfaces/recomendaciones";
import axios from "axios";
import { OpenAI } from "openai";

export const getCompletion = async (
  prompt: string,
  language: string | undefined,
  imageFile: File
): Promise<any> => {
  try {
    const formData = new FormData();
    formData.append("prompt", prompt);
    if (language) {
      formData.append("language", language);
    }

    if (imageFile) {
      formData.append("image", imageFile);
    }

    const response = await fetch(
      "http://localhost:8000/api/openai/completion",
      {
        method: "POST",
        body: formData,
      }
    );

    if (!response.ok) {
      throw new Error(`Error en la solicitud: ${response.statusText}`);
    }

    const result = await response.json();

    console.log("SERVICE", result);
    if (result.message) {
      return result;
    }

    const place: Place = {
      description_place:
        result.description_place || "Descripción no disponible",
      image: result.image || "URL de imagen no disponible",
      typical_food: result.typical_food || "Comida típica no disponible",
      languages: result.languages || "Idiomas no disponibles",
      traditional_music:
        result.traditional_music || "Música tradicional no disponible",
      city_tourist_map: "",
      map_of_tourist_places_in_ecuador: "",
      hotels: "",
      regions: result.regions || "Regiones no disponibles",
      location: result.location || "Ubicación no disponible",
      created_at: result.created_at || "Fecha de creación no disponible",
    };
    console.log("RESPUESTA oOK: ", place);
    return place;
  } catch (error) {
    console.error("Error fetching completion:", error);
    throw error;
  }
};

export async function getTouristPlaces(
  origen: string,
  opciones: string
): Promise<RecomendacionesCards> {
  let openai = new OpenAI({
    apiKey: process.env.VUE_APP_CHAT_GPT_KEY,
    dangerouslyAllowBrowser: true,
  });

  const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content: `Tu eres un asistente turistico que das recomendaciones de lugares turísticos en donde el usuario te mandara un nombre de una ciudad de origen o inicio y debes recomendar al menos 6 ciudades a las cuales es recomendable viajar desde la ciudad origen. 
                  Adicional el usuario te puede dar una opcion para que busques las ciudades de acuerdo a ese parametro, por ejemplo: Guayaquil: Internacional. Segun esta opcion tu debes buscar ciudades internacionales para recomendar.
                  Debes proporcionar un string de un arreglo de objetos json en este formato [{}, {}, {}], nada mas que eso lista para aplicar un JSON.parse 
                  con los siguientes campos: ciudad, gasto aproximado en dolares incluye el signo de la moneda de la ciudad de origen tambien asegurate de elegir calcular con opciones economicas y dependiendo del tiempo de viaje si se selecciona bus, vehiculo o avión, tiempo de viaje en un vehiculo o avion añadirlo en el string, y una pequeña descripción. Los nombres de las variables en el json son asi: ciudad, gasto, tiempo y descripcion respectivamente.
                  Trata de elegir al menos 4 ciudades nacionales y 2 internacionales, con excepción de las opciones 'Nacional' e 'Internacional', en estos casos lista todas las ciudades segun la opción.
                  El string no debe llevar nada de espacios ni saltos de linea, Asegúrate de que sea un JSON bien formado. Y asegurate de no pasar de mas de 900 tokens. Si no recibes ningun nombre de ninguna ciudad devuelve un arreglo vacio`,
      },
      {
        role: "user",
        content: "Guayaquil: Nacional",
      },
      {
        role: "assistant",
        content: `[{"ciudad": "Quito", "gasto": "$500", "tiempo": "8 horas en bus", "descripcion": "Conocida por su centro histórico, declarado Patrimonio de la Humanidad por la UNESCO."},{"ciudad": "Cuenca", "gasto": "$300", "tiempo": "4 horas en vehiculo", "descripcion": "Famosa por su arquitectura colonial española y sus ríos que atraviesan la ciudad."},{"ciudad": "Baños", "gasto": "$300", "tiempo": "6 horas en bus", "descripcion": "Conocida por sus aguas termales y su proximidad a la selva amazónica."},{"ciudad": "Salinas", "gasto": "$200", "tiempo": "2 horas en vehiculo", "descripcion": "Balneario en la costa de Ecuador, famoso por sus playas y deportes acuáticos."},{"ciudad": "Manta", "gasto": "$300", "tiempo": "5 horas en bus", "descripcion": "Ciudad portuaria en la costa de Ecuador, conocida por su industria pesquera y sus playas."},{"ciudad": "Loja", "gasto": "$300", "tiempo": "1 hora en avión", "descripcion": "Conocida por su rica tradición musical y cultural."}]`,
      },
      {
        role: "user",
        content: origen + ": " + opciones,
      },
    ],
    max_tokens: 900,
    temperature: 0.7,
  });

  console.log(completion);
  const data = JSON.parse(
    completion.choices[0].message.content?.trim()
      ? completion.choices[0].message.content
      : "[]"
  );
  console.log(data);

  return data;
}

export async function getEspecificCityData(
  origen: string,
  destino: string,
  idioma: string
): Promise<CiudadInfo> {
  let openai = new OpenAI({
    apiKey: process.env.VUE_APP_CHAT_GPT_KEY,
    dangerouslyAllowBrowser: true,
  });

  let instrucciones: string = "";

  if (idioma === "es") {
    instrucciones = `Tu eres un asistente turistico que das recomendaciones de lugares turísticos en donde el usuario te mandara un nombre de una ciudad de origen o inicio y de una ciudad destino. 
                  Como asistente debes proporcionar toda la informacion turistica que existe en la ciudad de destino. Pero tambien es necesario saber la ciudad de origen para poder dar una recomendacion mas precisa sobre los precios, tiempos y lugares de paso.
                  Tu respuesta sera un string de un arreglo de objetos json en este formato [{}, {}, {}], nada mas que eso lista para aplicar un JSON.parse 
                  A continucion te muestro los campos que enviaras, Primero estara la importancia del campo que esta rodeado de *, luego el nombre del campo estara entre () y si esa variable tiene mas campos estaras rodeados de [], 
                  Segun la importancia si es 
                  *Alta*=> el campo es obligatorio y tomara los tokens que se necesiten para dar una informacion completa del campo
                  *Media*=> el campo es obligatorio y su descripcion sera breve y precisa 
                  *Baja*=> el campo es opcional y solo se presenta si hay tokens disponibles despues de que los demas campos de importancia Alta y Media ya hayan sido definidos, en caso de que los demas campos hayan ocupado mas informacion los de importancia Baja no se presentan.
                  A continuacion los campos que enviaras: 
                  *Alta*(ciudad)=Sera un string del Nombre de la ciudad, 
                  *Alta*(transporte)=arreglo de strings de presupuesto en transporte en bus, avion y carro propio para dirigirse a la ciudad destino, incluir detalles del precio y tiempo de viaje. En caso de que uno de los valores no sea factible poner: No es factible, calcular valores del viaje de solo de ida. Si tienes la informacion de donde se toma el transporte o la compañia que ofrece el servicio incluirlo,
                  *Alta*(hotel)=gasto en hotel o estadia incluir precios de hoteles de 2 a 5 estrellas, 
                  *Alta*(comida)=gasto en comida dependiendo del tiempo de estadia, incluye detalles como desayuno, almuerzo y cena,
                  *Alta*(documentacion)=En caso de que se necesite algun tipo de documentacion para ingresar a la ciudad como pasaporte, visa, etc incluir el gasto segun el pais de la ciudad de origen,
                  *Alta*(duracion)=sera un string en donde muestras el tiempo recomendado de estadía y tambien recomendarias las mejores temporadas puedes incluir mas datos sobre este tema, tambien incluye en tiempo de viaje y desglosalo por el tipo de transporte, 
                  *Alta*(descripcion)=Sera un string y aqui describiras la ciudad y su importancia turistica y demas datos que interesaria a un usuario en busca de un viaje, 
                  *Alta*(lugares)=Sera un arreglo de strings en donde listaras todos los lugares a visitar y actividades a realizar.
                  *Media*(transp_local)=Sera un string en donde se muestra las opciones de transporte disponibles en la ciudad (metro, autobús, taxi, etc.) y el precio que estos tienen, mostrar ultimos precios y la fecha de estos registros,
                  *Alta*(clima)=string en donde se muestra el clima de la ciudad y las mejores temporadas para visitarla,
                  *Media*(seguridad)=string en donde se muestra la seguridad de la ciudad y recomendaciones para los turistas,
                  *Media*(idioma)=string en donde se muestra el idioma oficial de la ciudad y otros idiomas comunes,
                  *Alta*(moneda)=string en donde se muestra la moneda oficial de la ciudad y si es necesario cambiar dinero,
                  *Baja*(costumbres)=string en donde se muestra las costumbres y tradiciones de la ciudad,
                  *Media*(gastronomia)=string en donde se listaras los platos tipicos y recomendados para comprar en la visita,
                  *Baja*(compras)=string en donde listas los lugares de compras más populares de la ciudad y los productos típicos,
                  *Baja*(vida_nocturna)=string en dondelistas las zonas de vida nocturna más populares de la ciudad y las actividades más comunes,
                  *Alta*(alojamiento)=string en donde listas los alojamiento más populares de la ciudad y los precios aproximados, mostrar nombres especificos,
                  *Alta*(restaurantes)=string en donde listas los restaurantes más populares de la ciudad y los platos más recomendados, mostrar nombres de restaurantes mas visitados,
                  *Media*(actividades)=string en donde listas las actividades más populares de la ciudad y cómo participar en ellas,
                  *Baja*(consejos)=string en donde se muestra consejos útiles para los turistas que visitan la ciudad,
                  *Media*(telefono)=string en donde se muestra los números de teléfono de emergencia y de interés en la ciudad,
                  *Media*(salud)=string en donde se muestra la situación de la salud en la ciudad y si es necesario vacunarse antes de viajar,
                  *Baja*(comunicacion)=string en donde se muestra cómo comunicarse con los locales en la ciudad y si es necesario aprender algunas frases básicas,
                  Los string no debe llevar nada de espacios ni saltos de linea, Asegúrate de que sea un JSON bien formado. Y asegurate de no pasar de mas de 4000 tokens.
                  En caso de que no consigas informacion de algunos de los campos es preferible de que no envies el campo, recuerda no inventar informacion,
                  Para los casos como restaurantes, hoteles, lugares de compras es preferible que listes los nombres especificos.
                  Retornas solo un objeto json con los campos anteriores, no un arreglo de objetos json
                  El usuario te enviara la informacion de esta manera Origen,Destino`;
  } else {
    instrucciones = `You are a tourist assistant who provides recommendations for tourist destinations. The user will send you the name of a city of origin or start and a destination city. 
As an assistant, you must provide all the tourist information available for the destination city. However, it is also necessary to know the city of origin to give a more accurate recommendation regarding prices, travel times, and stopover locations.
Your response should be a string representing an array of JSON objects in the format [{}, {}, {}], ready for JSON.parse. 
Below are the fields you will send. First, the importance of the field is enclosed in *, followed by the field name in (), and if that variable has more fields, they will be enclosed in [].
According to the importance:
*High* => The field is mandatory and will take the tokens needed to give a complete description of the field.
*Medium* => The field is mandatory, but its description should be brief and precise.
*Low* => The field is optional and will only be included if there are tokens left after defining the High and Medium importance fields. If the High and Medium fields take up more information, the Low importance fields will not be included.
Here are the fields you will send: 
*High*(city) = A string with the name of the destination city.
*High*(transportation) = An array of strings showing transportation options by bus, plane, and car, including price details and travel time. If one of the values is not feasible, put: Not feasible. Calculate one-way trip costs. If you have information on where to take the transportation or the company offering the service, include it.
*High*(hotel) = The cost of the hotel or accommodation, including prices for 2 to 5-star hotels.
*High*(food) = The cost of food depending on the length of stay. Include details such as breakfast, lunch, and dinner.
*High*(documentation) = If any documentation is required to enter the city, such as a passport or visa, include the cost based on the country of origin.
*High*(duration) = A string showing the recommended length of stay and the best seasons to visit. Include travel time broken down by transportation type.
*High*(description) = A string describing the city, its tourist importance, and other information of interest to someone planning a trip.
*High*(places) = An array of strings listing all the places to visit and activities to do.
*Medium*(local_transport) = A string showing the available transportation options within the city (metro, bus, taxi, etc.) and their prices, with the most recent data available.
*High*(climate) = A string describing the city's climate and the best seasons to visit.
*Medium*(security) = A string showing the city's security situation and recommendations for tourists.
*Medium*(language) = A string showing the official language of the city and other common languages.
*High*(currency) = A string showing the city's official currency and whether currency exchange is needed.
*Low*(customs) = A string describing the city's customs and traditions.
*Medium*(gastronomy) = A string listing typical dishes and food recommended during the visit.
*Low*(shopping) = A string listing popular shopping locations and typical products to buy.
*Low*(nightlife) = A string listing popular nightlife areas and activities.
*High*(accommodation) = A string listing the most popular accommodations and approximate prices. Include specific names.
*High*(restaurants) = A string listing the most popular restaurants and recommended dishes. Include specific restaurant names.
*Medium*(activities) = A string listing the most popular activities and how to participate in them.
*Low*(tips) = A string providing useful tips for tourists visiting the city.
*Medium*(phone) = A string listing emergency and other important phone numbers in the city.
*Medium*(health) = A string showing the health situation in the city and whether vaccinations are necessary before traveling.
*Low*(communication) = A string explaining how to communicate with locals and whether it's necessary to learn basic phrases.
Ensure the strings do not contain spaces or line breaks. Make sure it is a well-formed JSON and does not exceed 4000 tokens.
If you cannot obtain information for some fields, it is preferable to omit the field. Do not invent information.
For cases like restaurants, hotels, and shopping locations, it is preferable to list specific names.
Return only one JSON object with the fields above, not an array of JSON objects.
The user will send the information in this format: Origin,Destination.`;
  }

  const completion = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content: instrucciones,
      },
      {
        role: "user",
        content: "Guayaquil,Cuenca",
      },
      {
        role: "assistant",
        content: `{"ciudad": "Cuenca","gasto": {"transporte": ["Bus: $20 en la terminal terrestre en ida y venida, $24 en ida y venida de cooperativas privadas", "Avión: 40$ aproximadamente, se toma 1 hora de viaje", "Carro propio: $50 si el coche consume 2l/km en ida y venida, "],"hotel": "$25 por noche en hotel de 2 estrellas, 40$ en hoteles de 3 estrellas","comida": "20$ por día","documentacion": "No se necesita documentación adicional"},"duracion": "4 días. Las mejores temporadas para visitar son de junio a septiembre.","descripcion": "Famosa por su arquitectura colonial española y sus ríos que atraviesan la ciudad.","lugares": ["Parque Nacional Cajas", "Catedral de la Inmaculada Concepción", "Museo Pumapungo", "El Barranco"],"transporte": "Metro, autobús, taxi","clima": "Templado. Las mejores temporadas para visitarla son de junio a septiembre.","seguridad": "Alta seguridad. Se recomienda tener precaución en áreas concurridas.","idioma": "Español. Otros idiomas comunes: Inglés","moneda": "Dólar estadounidense. No es necesario cambiar dinero.","costumbres": "Las costumbres incluyen festividades religiosas y celebraciones culturales.","gastronomia": "Gastronomía típica incluye platos como el cuy asado y el mote pillo.","cultura": "La cultura es rica en tradiciones y festividades como el Corpus Christi.","historia": "Cuenca tiene una rica historia colonial y es Patrimonio de la Humanidad por la UNESCO.","compras": "Lugares de compras populares incluyen mercados locales y tiendas de artesanías.","vida_nocturna": "Lugares de vida nocturna populares incluyen bares y discotecas en el centro histórico.","transporte_local": "Medios de transporte locales incluyen autobuses y taxis.","alojamiento": "Tipos de alojamiento populares incluyen hoteles y hostales. Precios aproximados: $50-$150 por noche.","restaurantes": "Restaurantes populares incluyen Tiesto's y Raymipampa. Platos recomendados: Cuy asado, Mote pillo.","actividades": "Actividades populares incluyen senderismo en el Parque Nacional Cajas y visitas a museos.","consejos": "Consejos útiles incluyen llevar ropa abrigada y estar preparado para la lluvia.","emergencias": "En caso de emergencias, llamar al 911.","telefono": "Números de teléfono de emergencia: 911. Otros números de interés: Policía: 101, Bomberos: 102.","salud": "La situación de la salud es buena. No es necesario vacunarse antes de viajar.","seguro": "Es recomendable contratar un seguro de viaje antes de visitar la ciudad.","comunicacion": "Es útil aprender algunas frases básicas en español para comunicarse con los locales."}`,
      },
      {
        role: "user",
        content: `${origen},${destino}`,
      },
    ],
    max_tokens: 4000,
    temperature: 0.8,
  });

  console.log(completion);
  const data = JSON.parse(
    completion.choices[0].message.content?.trim()
      ? completion.choices[0].message.content
      : "[]"
  );

  let resultado: any;

  if (Array.isArray(data)) {
    resultado = data.length > 0 ? data[0] : null;
  } else if (typeof data === "object" && data !== null) {
    resultado = data;
  } else {
    resultado = {};
  }
  console.log(resultado);

  return resultado;
}

export async function fetchCities(cityName: string) {
  let citiesList: string[] = [];

  if (cityName.length < 3) {
    return citiesList;
  }

  try {
    const response = await axios.get<GeoSearch[]>(
      "https://api.swiftcomplete.com/v1/places/",
      {
        params: {
          key: process.env.VUE_APP_GEO_CITIES,
          text: cityName,
          biasTowards: "51.50532341149335,-0.087890625",
          resultOrdering: "location_biasing",
          maxResults: 5,
        },
      }
    );

    citiesList = response.data.map(
      (result) => result.primary.text + ", " + result.secondary.text
    );

    citiesList = [...new Set(citiesList.filter((city) => city))];
  } catch (error) {
    citiesList = [];
    console.error("Error al obtener los datos:", error);
  }

  return citiesList;
}
