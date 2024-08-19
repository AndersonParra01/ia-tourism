import axios from "axios";
import { Place } from "./user";

const API_URL = "http://localhost:8000/api/places";

export const apiPlaceCreate = async (data: any): Promise<any> => {
  try {
    console.log("service", data);
    const response = await axios.post(API_URL + "/create", data);
    return response.data;
  } catch (error) {
    console.error("Error logging in:", error);
    throw error;
  }
};

export const apiPlaceById = async (id: number): Promise<any> => {
  try {
    const response = await axios.get(API_URL + "/get" + `/${id}`);
    return response.data;
  } catch (error) {
    console.error("Error logging in:", error);
    throw error;
  }
};
