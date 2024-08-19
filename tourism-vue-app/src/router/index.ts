import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import Map from "../components/Map.vue";
import Tourism from "@/components/tourism.vue";
import Recomendacion from "@/components/Recomendacion.vue";
import HistorialBusqueda from "@/components/HistorialBusqueda.vue";
import PlaceDetails from "@/components/PlaceDetails.vue";

const routes = [
  {
    path: "/",
    redirect: "/login", // Redirige a la ruta de login por defecto
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/map",
    name: "Map",
    component: Map,
  },
  {
    path: "/tourism",
    name: "Tourism",
    component: Tourism,
  },
  {
    path: "/historial-busquedas",
    name: "HistorialBusqueda",
    component: HistorialBusqueda,
  },
  {
    path: "/destino-favorito/:id",
    name: "DestinoFavorito",
    component: PlaceDetails,
  },
  {
    path: "/recomendaciones",
    name: "Recomendacion",
    component: Recomendacion,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
