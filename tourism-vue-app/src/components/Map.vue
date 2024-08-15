<template>
    <div style="height: 55vh; width: 30vw;">
      <l-map style="height: 100%; width: 100%" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" />
        <l-marker
          v-for="place in places"
          :key="place.id"
          :lat-lng="[place.lat, place.lng]"
        >
          <l-popup>{{ place.name }}</l-popup>
        </l-marker>
      </l-map>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { LMap, LTileLayer, LMarker, LPopup } from 'vue3-leaflet';
  import 'leaflet/dist/leaflet.css';
  import axios from 'axios';
  
  export default {
    components: { LMap, LTileLayer, LMarker, LPopup },
    setup() {
      const zoom = ref(7);
      const center = ref([-1.7672, -78.8171]); // Coordenadas de Chimborzo, Ecuador
      const url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
      const places = ref([]);
  
      const fetchPlaces = async () => {
        try {
          // const response = await axios.get('URL_DE_LA_API');
          // places.value = response.data.results.map(place => ({
          //   id: place.id,
          //   lat: place.geometry.location.lat,
          //   lng: place.geometry.location.lng,
          //   name: place.name
          // }));
        } catch (error) {
          console.error('Error fetching places:', error);
        }
      };
  
      onMounted(() => {
        fetchPlaces();
      });
  
      return { zoom, center, url, places };
    }
  };
  </script>
  