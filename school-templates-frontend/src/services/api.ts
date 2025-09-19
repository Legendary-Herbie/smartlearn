import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE,
  headers: { "Content-Type": "application/json" },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  if (token && config.headers) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export default {
  login: (data: { username: string; password: string }) => api.post("/token/", data),
  refresh: (data: { refresh: string }) => api.post("/token/refresh/", data),
  register: (data: any) => api.post("/auth/register/", data),
  me: () => api.get("/auth/me/"),
  updateProfile: (data: FormData) => api.put("/auth/me/", data, { headers: { "Content-Type": "multipart/form-data" } }),
  plans: {
    list: () => api.get("/plans/"),
    create: (d: any) => api.post("/plans/", d),
  },
  flashcards: {
    list: () => api.get("/flashcards/"),
    create: (d: any) => api.post("/flashcards/", d),
  },
};
import axios from 'axios';

const API_BASE_URL = 'https://api.example.com'; // Replace with your actual API base URL

export const fetchSchools = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/schools`);
        return response.data;
    } catch (error) {
        console.error('Error fetching schools:', error);
        throw error;
    }
};

export const fetchSchoolById = async (id) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/schools/${id}`);
        return response.data;
    } catch (error) {
        console.error(`Error fetching school with id ${id}:`, error);
        throw error;
    }
};

// Add more API functions as needed
