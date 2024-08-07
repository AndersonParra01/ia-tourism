import axios from "axios";

const API_URL = "http://localhost:8000/api/openai/completion";

export const getCompletion = async (prompt: string): Promise<any> => {
  try {
    const response = await axios.get(`${API_URL}?prompt=${prompt}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching completion:", error);
    throw error;
  }
};
