interface RecomendacionesCards {
    ciudad: string,
    gasto: string,
    tiempo: string,
    descripcion: string
}

interface CiudadInfo {
    ciudad?: string;
    gasto?: {
      transporte?: string[];
      hotel?: string;
      comida?: string;
      documentacion?: string;
    };
    duracion?: string;
    descripcion?: string;
    lugares?: string[];
    transporte?: string;
    clima?: string;
    seguridad?: string;
    idioma?: string;
    moneda?: string;
    costumbres?: string;
    gastronomia?: string;
    cultura?: string;
    historia?: string;
    turismo?: string;
    compras?: string;
    vida_nocturna?: string;
    transporte_local?: string;
    alojamiento?: string;
    restaurantes?: string;
    actividades?: string;
    consejos?: string;
    emergencias?: string;
    telefono?: string;
    electricidad?: string;
    salud?: string;
    seguro?: string;
    comunicacion?: string;
    trans_aeropuerto?: string;
    trans_publico?: string;
    trans_privado?: string;
    trans_turistico?: string;
  }