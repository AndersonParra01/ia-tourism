import axios from "axios";

export interface Place {
  id: number;
  description_place: string | null;
  typical_food: string | null;
  languages: string | null;
  traditional_music: string | null;
  city_tourist_map: string | null;
  map_of_tourist_places_in_ecuador: string | null;
  hotels: string | null;
  regions: string | null;
  created_at: string;
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

export const fetchUserPlace = async (userId: number, placeId: number) => {
  try {
    const url = "http://localhost:8000/api/users/addToPlace";
    const response = await axios.post(url, {
      place_id: placeId,
      user_ids: userId,
    });
    return response.data;
  } catch (error) {
    console.log("Error fetching user place:", error);
    throw error;
  }
};

export const fetchUserPlaceDelete = async (userId: number, placeId: number) => {
  try {
    const url = "http://localhost:8000/api/users/remove-users-from-place";
    const response = await axios.post(url, {
      place_id: placeId,
      user_ids: userId,
    });
    return response.data;
  } catch (error) {
    console.log("Error fetching user place:", error);
    throw error;
  }
};
