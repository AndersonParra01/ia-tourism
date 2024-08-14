import axios from "axios";

const api = axios.create({
  baseURL: process.env.VITE_API_URL,
  // headers: {
  //   'Authorization': `Bearer ${import.meta.env.VITE_API_KEY}`
  // }
});

export const apiLogin = async (userName: string, password: string) => {
  const response = await api.post("/login", { userName, password });
  return response.data;
};
