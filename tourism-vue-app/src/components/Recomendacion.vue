<template>
  <div class="container flex flex-col items-center justify-center gap-8 bg p-4">
    <div class="flex flex-col items-center mt-2 p-8 bg-white shadow-md rounded-lg">
      <div class="flex space-x-4 mb-4">
        <div class="relative">
          <input v-model="origen" @input="fetchCitiesO" placeholder="Origen" autocomplete="off"
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
          <ul v-if="citiesO.length"
            class="absolute left-0 w-full mt-2 bg-white border border-gray-300 rounded-lg shadow-lg z-10">
            <li v-for="(city, index) in citiesO" :key="index" @click="selectOrigen(city)"
              class="px-3 py-2 hover:bg-gray-100 cursor-pointer">
              {{ city }}
            </li>
          </ul>
        </div>
        <div class="relative">
          <input v-model="destino" @input="fetchCitiesD" placeholder="Destino" autocomplete="off"
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
          <ul v-if="citiesD.length"
            class="absolute left-0 w-full mt-2 bg-white border border-gray-300 rounded-lg shadow-lg z-10">
            <li v-for="(city, index) in citiesD" :key="index" @click="selectDestino(city)"
              class="px-3 py-2 hover:bg-gray-100 cursor-pointer">
              {{ city }}
            </li>
          </ul>
        </div>
        <button @click="getPlaces"
          class="px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-200">
          Buscar
        </button>
      </div>
      <div class="w-full">
        <select v-model="selectedOption"
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300">
          <option v-for="option in options" :key="option" :value="option">{{ option }}</option>
        </select>
      </div>
    </div>

    <div v-if="loading">Cargando...</div>
    <div v-else class="cards-container">
      <div v-for="card in cards" :key="card.ciudad" class="card" @click="getPlaceFromRecommendation(card)"
        :class="{ disabled: globalClicked }">
        <h3>{{ card.ciudad }}</h3>
        <p>Gasto Aprox: {{ card.gasto }}</p>
        <p>Tiempo: {{ card.tiempo }}</p>
        <p>{{ card.descripcion }}</p>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      @click="handleClickOutside">
      <div class="bg-white rounded-lg shadow-lg p-8 w-full max-w-3xl relative" @click.stop
        style="max-height: 90vh; overflow-y: auto;">
        <button class="absolute top-2 right-2 text-gray-600 hover:text-gray-800 focus:outline-none" @click="closeModal">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"
            stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <h3 class="text-2xl font-bold mb-4 text-gray-800">{{ selectedCard.ciudad }}</h3>

        <div class="details space-y-4">
          <div v-if="selectedCard.transporte">
            <p class="font-semibold text-lg">Gasto en transporte:</p>
            <ul class="list-disc list-inside text-gray-700">
              <li v-for="item in selectedCard.transporte" :key="item">{{ item }}</li>
            </ul>
          </div>

          <p v-if="selectedCard.hotel" class="text-gray-700"><b>Gastos Hospedaje:</b> {{ selectedCard.hotel }}</p>
          <p v-if="selectedCard.comida" class="text-gray-700"><b>Gasto en comidas:</b> {{ selectedCard.comida }}</p>
          <p v-if="selectedCard.documentacion" class="text-gray-700"><b>Documentación necesaria:</b> {{
            selectedCard.documentacion }}</p>
          <p v-if="selectedCard.duracion" class="text-gray-700"><b>Duración de viaje:</b> {{ selectedCard.duracion }}
          </p>
          <p v-if="selectedCard.descripcion" class="text-gray-700"><b>Descripción:</b> {{ selectedCard.descripcion }}
          </p>
          <p v-if="selectedCard.lugares" class="text-gray-700"><b>Lugares:</b> {{ selectedCard.lugares.join(', ') }}</p>
          <p v-if="selectedCard.transp_local" class="text-gray-700"><b>Transporte Local:</b> {{
            selectedCard.transp_local }}</p>
          <p v-if="selectedCard.clima" class="text-gray-700"><b>Clima:</b> {{ selectedCard.clima }}</p>
          <p v-if="selectedCard.seguridad" class="text-gray-700"><b>Seguridad:</b> {{ selectedCard.seguridad }}</p>
          <p v-if="selectedCard.idioma" class="text-gray-700"><b>Idioma:</b> {{ selectedCard.idioma }}</p>
          <p v-if="selectedCard.moneda" class="text-gray-700"><b>Moneda:</b> {{ selectedCard.moneda }}</p>
          <p v-if="selectedCard.costumbres" class="text-gray-700"><b>Costumbres:</b> {{ selectedCard.costumbres }}</p>
          <p v-if="selectedCard.gastronomia" class="text-gray-700"><b>Gastronomía:</b> {{ selectedCard.gastronomia }}
          </p>
          <p v-if="selectedCard.cultura" class="text-gray-700"><b>Cultura:</b> {{ selectedCard.cultura }}</p>
          <p v-if="selectedCard.historia" class="text-gray-700"><b>Historia:</b> {{ selectedCard.historia }}</p>
          <p v-if="selectedCard.turismo" class="text-gray-700"><b>Turismo:</b> {{ selectedCard.turismo }}</p>
          <p v-if="selectedCard.compras" class="text-gray-700"><b>Compras:</b> {{ selectedCard.compras }}</p>
          <p v-if="selectedCard.vida_nocturna" class="text-gray-700"><b>Vida Nocturna:</b> {{ selectedCard.vida_nocturna
            }}</p>
          <p v-if="selectedCard.transporte_local" class="text-gray-700"><b>Transporte Local:</b> {{
            selectedCard.transporte_local }}</p>
          <p v-if="selectedCard.alojamiento" class="text-gray-700"><b>Alojamiento:</b> {{ selectedCard.alojamiento }}
          </p>
          <p v-if="selectedCard.restaurantes" class="text-gray-700"><b>Restaurantes:</b> {{ selectedCard.restaurantes }}
          </p>
          <p v-if="selectedCard.actividades" class="text-gray-700"><b>Actividades:</b> {{ selectedCard.actividades }}
          </p>
          <p v-if="selectedCard.consejos" class="text-gray-700"><b>Consejos:</b> {{ selectedCard.consejos }}</p>
          <p v-if="selectedCard.emergencias" class="text-gray-700"><b>Emergencias:</b> {{ selectedCard.emergencias }}
          </p>
          <p v-if="selectedCard.telefono" class="text-gray-700"><b>Teléfono:</b> {{ selectedCard.telefono }}</p>
          <p v-if="selectedCard.salud" class="text-gray-700"><b>Salud:</b> {{ selectedCard.salud }}</p>
          <p v-if="selectedCard.seguro" class="text-gray-700"><b>Seguro:</b> {{ selectedCard.seguro }}</p>
          <p v-if="selectedCard.comunicacion" class="text-gray-700"><b>Comunicación:</b> {{ selectedCard.comunicacion }}
          </p>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
import { getTouristPlaces, getEspecificCityData, fetchCities } from '../services/ia';

export default {
  data() {
    return {
      origen: '',
      destino: '',
      selectedOption: 'Nacional',
      options: ['Nacional', 'Economico', 'Historico', 'Cultural', 'Diversión', 'Internacional'],
      touristPlaces: [],
      card: [],
      loading: false,
      showModal: false,
      selectedCard: {},
      citiesO: [],
      citiesD: [],
      globalClicked: false,
    };
  },
  methods: {
    async openModal(card) {
      this.selectedCard = card;
      this.showModal = true;
    },
    closeModal() {
      console.log('Cerrando modal');
      this.showModal = false;
    },
    handleClickOutside(event) {
      // Cierra el modal si el clic ocurre fuera del contenido del modal
      if (event.target === event.currentTarget) {
        this.closeModal();
      }
    },
    async getPlaces() {
      this.loading = true;
      try {
        if (this.origen === '') {
          alert('Por favor, ingrese un origen');
          return;
        }

        if (this.origen !== '' && this.destino !== '') {
          console.log('Destino:', this.destino);
          const modalData = await getEspecificCityData(this.origen, this.destino);
          this.openModal(modalData);
          return;
        }

        const places = await getTouristPlaces(this.origen, this.selectedOption);
        this.cards = places;
      } catch (error) {
        console.error('Hubo un error:', error);
      } finally {
        this.loading = false;
      }
    },
    async fetchCitiesO() {
      this.citiesO = await fetchCities(this.origen);
    },
    async fetchCitiesD() {
      this.citiesD = await fetchCities(this.destino);
    },
    async getPlaceFromRecommendation(card) {
      if (!this.globalClicked) {
        this.loading = true;
        this.globalClicked = true;
        try {
          const modalData = await getEspecificCityData(this.origen, card.ciudad);
          console.log('Modal Data:', modalData);
          this.openModal(modalData);
          return;
        } catch (error) {
          console.error('Hubo un error:', error);
        } finally {
          this.loading = false;
          this.globalClicked = false;
        }
      }
    },
    selectOrigen(city) {
      console.log('origen', city);
      this.origen = city;
      this.citiesO = []; // Limpia las sugerencias después de seleccionar
    },
    selectDestino(city) {
      console.log('destino', city);
      this.destino = city;
      this.citiesD = []; // Limpia las sugerencias después de seleccionar
    },
  },
};
</script>

<style scoped>
.input-container {
  display: flex;
  gap: 20px;
}

input {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #ccc;
  font-size: 1.1em;
  width: 200px;
}

select {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #ccc;
  font-size: 1.1em;
  width: 220px;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(3, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 50px;
  width: 80%;
}

.card {
  background-color: white;
  border: 1px solid #ddd;
  padding: 16px;
  margin: 16px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.2s ease-in-out;
}

.card:hover {
  transform: translateY(-10px);
}

.card h3 {
  font-size: 1.5em;
  margin-bottom: 10px;
  color: #333;
}

.card p {
  font-size: 1em;
  color: #666;
}

.styled-button {
  background-color: #007BFF;
  /* Primary blue color */
  color: white;
  /* White text */
  border: none;
  /* Remove default border */
  padding: 10px 20px;
  /* Add some padding */
  font-size: 16px;
  /* Increase font size */
  border-radius: 5px;
  /* Rounded corners */
  cursor: pointer;
  /* Pointer cursor on hover */
  transition: background-color 0.3s ease;
  /* Smooth transition for background color */
  height: 45px;
  margin-left: 15px;
}

.styled-button:hover {
  background-color: #0056b3;
  /* Darker blue on hover */
}

.modal {
  display: flex;
  /* Asegúrate de que esté visible */
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1000;
  /* Aumenta el z-index para que esté encima de otros elementos */
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
  opacity: 1;
  /* Asegura la opacidad */
  transition: opacity 0.3s ease-in-out;
  /* Transición suave */
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 600px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  opacity: 1;
  /* Asegura la opacidad */
  transition: opacity 0.3s ease-in-out;
  pointer-events: auto;
  z-index: 1001;
  position: relative;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  pointer-events: auto;
  z-index: 1002;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

h3 {
  color: #333;
  font-size: 24px;
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  color: #666;
  font-size: 16px;
  margin: 5px 0;
}

.details p {
  color: #666;
  font-size: 16px;
  margin: 5px 0;
}

.details span {
  margin-right: 5px;
}

.autocomplete-container {
  position: relative;
  display: flex;
  gap: 20px;
  width: 45%;
  /* Ancho del contenedor del input */
}

input {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #ccc;
  font-size: 1.1em;
  width: 100%;
  /* El input ocupa todo el ancho del contenedor */
}

.autocomplete-list {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  max-height: 150px;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 0 0 8px 8px;
  overflow-y: auto;
  list-style: none;
  padding: 0;
  margin: 0;
  z-index: 1000;
}

.autocomplete-list li {
  padding: 10px;
  cursor: pointer;
}

.autocomplete-list li:hover {
  background-color: #f0f0f0;
}
</style>
