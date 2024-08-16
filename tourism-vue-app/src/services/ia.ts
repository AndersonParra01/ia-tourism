export interface Place {
  description: string;
  image: string;
  location: string;
  typicalFood: string;
  languages: string;
  traditionalMusic: string;
  regions: string;
}

export const getCompletion = async (prompt: string): Promise<Place> => {
  try {
    const response = await fetch(
      `http://localhost:8000/api/openai/completion?prompt=${encodeURIComponent(
        prompt
      )}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    if (!response.ok) {
      throw new Error(`Error en la solicitud: ${response.statusText}`);
    }

    const result = await response.json();

    // Transformamos la respuesta en el formato que necesitamos
    const place: Place = {
      description: result.description_place || "Descripción no disponible",
      image:
        result[" 'image': generate_image, location"] ||
        "URL de imagen no disponible",
      location: result.location || "Ubicación no disponible",
      typicalFood: result.typical_food || "Comida típica no disponible",
      languages: result.languages || "Idiomas no disponibles",
      traditionalMusic:
        result.traditional_music || "Música tradicional no disponible",
      regions: result.regions || "Regiones no disponibles",
    };

    return place;
  } catch (error) {
    console.error("Error fetching completion:", error);
    throw error;
  }
};
