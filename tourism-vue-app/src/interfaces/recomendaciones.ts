export interface RecomendacionesCards {
    ciudad: string,
    gasto: string,
    tiempo: string,
    descripcion: string
}

export interface CiudadInfo {
    ciudad?: string;
    transporte?: string[];
    hotel?: string;
    comida?: string;
    documentacion?: string;
    duracion?: string;
    descripcion?: string;
    lugares?: string[];
    transp_local?: string;
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

export interface GeoSearch {
    primary:     Ary;
    secondary:   Ary;
    type:        string;
    isContainer: boolean;
    distance:    Distance;
    countryCode: string;
}

export interface Distance {
    units:       string;
    measurement: number;
    type:        string;
    geometry:    Geometry;
}

export interface Geometry {
    centre: Centre;
}

export interface Centre {
    lat: number;
    lon: number;
}

export interface Ary {
    text:       string;
    highlights: number[];
}
