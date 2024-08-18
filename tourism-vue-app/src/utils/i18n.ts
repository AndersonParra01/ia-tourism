import { createI18n } from "vue-i18n";

const messages = {
  en: {
    welcome: "OpenAI Virtual Tourism Assistant Ec",
    selectLanguage: "Select your language:",
    generalSearch: "General Search",
    favoriteDestinations: "Search Favorite Destinations",
    enterPlace: "Enter the tourist place",
    send: "Send",
    loading: "Loading...",
    noResults: "No results found",
    mapTouristImage: "Tourist Map and Image",
    descriptionPlace: "Place Description",
    typicalFood: "Typical Food",
    languages: "Languages",
    traditionalMusic: "Traditional Music",
    regions: "Regions Associated",
    hotelsNearby: "Nearby Hotels",
    deleteSelected: "Delete Selected",
    home: "Home",
    searchHistory: "Search History",
    emptyPlace: "Empty place",
    login: "Login",
    register: "Register",
    logout: "Logout",
    search: "Search",
    username: "Username",
    password: "Password",
    dontHaveAccount: "Don't have an account?",
    registerHere: "Register here",
    loginError: "Login error",
    enterUsername: "Enter your username",
    enterPassword: "Enter your password",
    name: "Name",
    lastName: "Last Name",
    confirmPassword: "Confirm Password",
    alreadyHaveAccount: "Already have an account?",
    registerSuccess: "Registration successful",
    passwordsDoNotMatch: "Passwords do not match",
    recommendationHistory: "Recommendation History",
    delete: "Delete",
    time: "Time",
    origin: "Origin",
    destination: "Destination",
    searchButton: "Search",
    expense: "Approximate Expense:",
    description: "Description:",
    close: "Close",
    details: {
      transportExpense: "Transport Expense:",
      lodgingExpense: "Lodging Expense:",
      foodExpense: "Food Expense:",
      documentation: "Required Documentation:",
      tripDuration: "Trip Duration:",
      places: "Places:",
      localTransport: "Local Transport:",
      climate: "Climate:",
      security: "Security:",
      language: "Language:",
      currency: "Currency:",
      customs: "Customs:",
      gastronomy: "Gastronomy:",
      culture: "Culture:",
      history: "History:",
      tourism: "Tourism:",
      shopping: "Shopping:",
      nightlife: "Nightlife:",
      localTransportDetails: "Local Transport:",
      accommodation: "Accommodation:",
      restaurants: "Restaurants:",
      activities: "Activities:",
      tips: "Tips:",
      emergencies: "Emergencies:",
      phone: "Phone:",
      health: "Health:",
      insurance: "Insurance:",
      communication: "Communication:",
    },
    assistantResponse: "Assistant Response",
    placeInformation: "Place Information",
    message: "Message",
    saveConsultation: "Save Consultation",
    loginRequired: "You must be logged in to save the consultation",
    saveSuccess: "Saved successfully",
    saveError: "Error saving history",
    clearButton: "Clear",
    destineTuristico: "Tourist Destination",
    save: "Save",
  },
  es: {
    welcome: "OpenAI Asistente de Turismo Virtual Ec",
    selectLanguage: "Seleccione su idioma:",
    generalSearch: "Búsqueda General",
    favoriteDestinations: "Buscar Destinos Favoritos",
    enterPlace: "Selecciona tu lugar turístico",
    send: "Enviar",
    loading: "Cargando...",
    noResults: "No se encontraron resultados",
    mapTouristImage: "Mapa Turístico e Imagen",
    descriptionPlace: "Descripción del Lugar",
    typicalFood: "Comida Típica",
    languages: "Idiomas",
    traditionalMusic: "Música Tradicional",
    regions: "Regiones Asociadas",
    hotelsNearby: "Hoteles Cercanos",
    deleteSelected: "Eliminar Seleccionados",
    home: "Inicio",
    searchHistory: "Historial de Búsquedas",
    emptyPlace: "Lugar vacío",
    login: "Iniciar Sesión",
    logout: "Salir",
    search: "Buscar",
    username: "Usuario",
    password: "Contraseña",
    dontHaveAccount: "¿No tienes cuenta?",
    registerHere: "Regístrate aquí",
    loginError: "Error al iniciar sesión",
    enterUsername: "Ingresa tu nombre de usuario",
    enterPassword: "Ingresa tu contraseña",
    name: "Nombre",
    lastName: "Apellido",
    confirmPassword: "Confirmar contraseña",
    alreadyHaveAccount: "¿Ya tienes una cuenta?",
    register: "Registrarse",
    registerSuccess: "Registro exitoso",
    passwordsDoNotMatch: "Las contraseñas no coinciden",
    recommendationHistory: "Historial de Recomendaciones",
    delete: "Eliminar",
    time: "Hora",
    origin: "Origen",
    destination: "Destino",
    expense: "Gasto Aprox:",
    description: "Descripción:",
    close: "Cerrar",
    searchButton: "Buscar",
    details: {
      transportExpense: "Gasto en transporte:",
      lodgingExpense: "Gastos Hospedaje:",
      foodExpense: "Gasto en comidas:",
      documentation: "Documentación necesaria:",
      tripDuration: "Duración de viaje:",
      places: "Lugares:",
      localTransport: "Transporte Local:",
      climate: "Clima:",
      security: "Seguridad:",
      language: "Idioma:",
      currency: "Moneda:",
      customs: "Costumbres:",
      gastronomy: "Gastronomía:",
      culture: "Cultura:",
      history: "Historia:",
      tourism: "Turismo:",
      shopping: "Compras:",
      nightlife: "Vida Nocturna:",
      localTransportDetails: "Transporte Local:",
      accommodation: "Alojamiento:",
      restaurants: "Restaurantes:",
      activities: "Actividades:",
      tips: "Consejos:",
      emergencies: "Emergencias:",
      phone: "Teléfono:",
      health: "Salud:",
      insurance: "Seguro:",
      communication: "Comunicación:",
    },
    assistantResponse: "Respuesta del Asistente",
    placeInformation: "Información del Lugar",
    message: "Mensaje",
    saveConsultation: "Guardar Consulta",
    loginRequired: "Debes iniciar sesión para guardar la consulta",
    saveSuccess: "Guardado correctamente",
    saveError: "Error al registrar historial",
    clearButton: "Limpiar",
    destineTuristico: "Destino Turístico",
    save: "Guardar",
  },
};

const i18n = createI18n({
  locale: "es",
  fallbackLocale: "en",
  messages,
});

export default i18n;
