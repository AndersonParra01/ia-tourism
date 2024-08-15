import axios from "axios";

const API_URL = "http://localhost:8000/api/auth";

export const apiLogin = async (username: string, password: string): Promise<any> => {
  try {  
    const response = await axios.post(API_URL + "/login", { username, password });
    return response.data;
  } catch (error) {
    console.error("Error logging in:", error);
    throw error;
  }
};

export const apiRegister = async (user:any): Promise<any> => {
  try {  
    console.log(user);
    const response = await axios.post(API_URL + "/register", { 
      names: user.names,
      lastnames: user.lastnames,
      username: user.username,
      password: user.password,
    });
    console.log(response);
    return response.data;
  } catch (error) {
    console.error("Error Register in:", error);
    throw error;
  }
};