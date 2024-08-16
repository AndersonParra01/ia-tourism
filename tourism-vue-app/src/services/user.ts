import axios from "axios";

export interface Place {
  id: number;
  name: string;
  description: string;
  location: string;
}

export interface User {
  id: number;
  username: string;
  names: string;
  lastnames: string;
  places: Place[];
}

export const fetchUserPlaces = async (userId: string): Promise<User> => {
  try {
    const url = `/api/users/get/${userId}`;
    console.log("URL:", url);
    const response = await axios.get(url);
    console.log("Response Data:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error fetching user places:", error);
    throw error;
  }
};
