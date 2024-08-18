<template>
  <div class="flex flex-col items-center justify-center gap-8 p-4">
    <div class="flex flex-col items-center mt-2 p-8 bg-white shadow-md rounded-lg w-full max-w-3xl">
      <div class="flex justify-center flex-row space-y-4 sm:space-y-0 sm:space-x-4 mb-4 w-full">
        <div class="relative w-full sm:w-1/2 mb-4 sm:mb-0">
          <input v-model="origen" @input="fetchCitiesO" :placeholder="$t('origin')" autocomplete="off"
            class="w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
          <ul v-if="citiesO.length"
            class="absolute left-0 w-full mt-2 bg-white border border-gray-300 rounded-lg shadow-lg z-10">
            <li v-for="(city, index) in citiesO" :key="index" @click="selectOrigen(city)"
              class="px-3 py-2 hover:bg-gray-100 cursor-pointer">
              {{ city }}
            </li>
          </ul>
        </div>
        <div class="relative w-full sm:w-1/2">
          <input v-model="destino" @input="fetchCitiesD" :placeholder="$t('destination')" autocomplete="off"
            class="w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
          <ul v-if="citiesD.length"
            class="absolute left-0 w-full mt-2 bg-white border border-gray-300 rounded-lg shadow-lg z-10">
            <li v-for="(city, index) in citiesD" :key="index" @click="selectDestino(city)"
              class="px-3 py-2 hover:bg-gray-100 cursor-pointer">
              {{ city }}
            </li>
          </ul>
        </div>
      </div>
      <div class="w-full mb-4">
        <select v-model="selectedOption"
          class="w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring focus:border-blue-300">
          <option v-for="option in options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>
      </div>
      <div class="flex w-full space-x-2">
        <button @click="getPlaces"
          class="w-full px-4 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-200">
          {{ $t("searchButton") }}
        </button>
        <button @click="clearInputs"
          class="w-full px-4 py-3 bg-red-500 text-white font-semibold rounded-lg hover:bg-red-700 transition duration-200">
          {{ $t("clearButton") }}
        </button>
      </div>
    </div>

    <div v-if="loading" class="text-center text-gray-600 mt-4">
      {{ $t("loading") }}
    </div>
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-8 w-full max-w-5xl">
      <div v-for="card in cards" :key="card.ciudad"
        class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition duration-200 cursor-pointer"
        @click="getPlaceFromRecommendation(card)" :class="{ disabled: globalClicked }">
        <h3 class="text-xl font-semibold text-gray-800 mb-2">
          {{ card.ciudad }}
        </h3>
        <p class="text-gray-600">{{ $t("expense") }}: {{ card.gasto }}</p>
        <p class="text-gray-600">{{ $t("time") }}: {{ card.tiempo }}</p>
        <p class="text-gray-600">{{ card.descripcion }}</p>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      @click="handleClickOutside">
      <div class="bg-white rounded-lg shadow-lg p-8 w-full max-w-3xl relative" @click.stop
        style="max-height: 90vh; overflow-y: auto">
        <button class="absolute top-2 right-2 text-gray-600 hover:text-gray-800 focus:outline-none" @click="closeModal">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"
            stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <h3 class="text-2xl font-bold mb-4 text-gray-800 text-center">
          {{ $t("destineTuristico") }} "{{ selectedCard.ciudad }}"
        </h3>

        <div class="flex justify-end m-4">
          <button @click="saveInfo"
            class="bg-blue-500 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg shadow">
            {{ $t("save") }}
          </button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-if="selectedCard.transporte" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.transportExpense") }}
            </p>
            <ul class="list-disc list-inside text-gray-700">
              <li v-for="item in selectedCard.transporte" :key="item">
                {{ item }}
              </li>
            </ul>
          </div>

          <div v-if="selectedCard.hotel" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.lodgingExpense") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.hotel }}</p>
          </div>

          <div v-if="selectedCard.comida" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.foodExpense") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.comida }}</p>
          </div>

          <div v-if="selectedCard.documentacion" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.documentation") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.documentacion }}</p>
          </div>

          <div v-if="selectedCard.duracion" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.tripDuration") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.duracion }}</p>
          </div>

          <div v-if="selectedCard.descripcion" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">{{ $t("description") }}</p>
            <p class="text-gray-700">{{ selectedCard.descripcion }}</p>
          </div>

          <div v-if="selectedCard.lugares" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.places") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.lugares.join(", ") }}</p>
          </div>

          <div v-if="selectedCard.transp_local" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.localTransport") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.transp_local }}</p>
          </div>

          <div v-if="selectedCard.clima" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.climate") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.clima }}</p>
          </div>

          <div v-if="selectedCard.seguridad" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.security") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.seguridad }}</p>
          </div>

          <div v-if="selectedCard.idioma" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.language") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.idioma }}</p>
          </div>

          <div v-if="selectedCard.moneda" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.currency") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.moneda }}</p>
          </div>

          <div v-if="selectedCard.costumbres" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.customs") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.costumbres }}</p>
          </div>

          <div v-if="selectedCard.gastronomia" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.gastronomy") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.gastronomia }}</p>
          </div>

          <div v-if="selectedCard.cultura" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.culture") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.cultura }}</p>
          </div>

          <div v-if="selectedCard.historia" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.history") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.historia }}</p>
          </div>

          <div v-if="selectedCard.turismo" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.tourism") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.turismo }}</p>
          </div>

          <div v-if="selectedCard.compras" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.shopping") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.compras }}</p>
          </div>

          <div v-if="selectedCard.vida_nocturna" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.nightlife") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.vida_nocturna }}</p>
          </div>

          <div v-if="selectedCard.transporte_local" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.localTransportDetails") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.transporte_local }}</p>
          </div>

          <div v-if="selectedCard.alojamiento" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.accommodation") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.alojamiento }}</p>
          </div>

          <div v-if="selectedCard.restaurantes" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.restaurants") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.restaurantes }}</p>
          </div>

          <div v-if="selectedCard.actividades" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.activities") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.actividades }}</p>
          </div>

          <div v-if="selectedCard.consejos" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">{{ $t("details.tips") }}</p>
            <p class="text-gray-700">{{ selectedCard.consejos }}</p>
          </div>

          <div v-if="selectedCard.emergencias" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.emergencies") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.emergencias }}</p>
          </div>

          <div v-if="selectedCard.telefono" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">{{ $t("details.phone") }}</p>
            <p class="text-gray-700">{{ selectedCard.telefono }}</p>
          </div>

          <div v-if="selectedCard.salud" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.health") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.salud }}</p>
          </div>

          <div v-if="selectedCard.seguro" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.insurance") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.seguro }}</p>
          </div>

          <div v-if="selectedCard.comunicacion" class="bg-gray-100 p-4 rounded-lg shadow">
            <p class="text-gray-700 font-semibold">
              {{ $t("details.communication") }}
            </p>
            <p class="text-gray-700">{{ selectedCard.comunicacion }}</p>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {
  getTouristPlaces,
  getEspecificCityData,
  fetchCities,
} from "../services/ia";
import { defineComponent, onMounted, ref, watch } from "vue";
import { apiPlaceCreate } from "./../services/place";
import { fetchUserPlace } from "./../services/user";
import { useRouter } from 'vue-router';
export default {
  setup() {
    const router = useRouter();

    const origen = ref("");
    const destino = ref("");
    const selectedOption = ref("Nacional");

    const clearInputs = () => {
      origen.value = "";
      destino.value = "";
    };

    return {
      origen,
      destino,
      selectedOption,
      clearInputs,
      router
    };
  },
  data() {
    return {
      options: [
        "Nacional",
        "Economico",
        "Historico",
        "Cultural",
        "Diversión",
        "Internacional",
      ],
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
      console.log("Cerrando modal");
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
        if (this.origen === "") {
          alert("Por favor, ingrese un origen");
          return;
        }

        if (this.destino === "") {
          alert("Por favor, ingrese un destino");
          return;
        }

        if (this.origen !== "" && this.destino !== "") {
          console.log("Destino:", this.destino);
          const modalData = await getEspecificCityData(
            this.origen,
            this.destino
          );
          this.openModal(modalData);
          return;
        }

        const places = await getTouristPlaces(this.origen, this.selectedOption);
        this.cards = places;
      } catch (error) {
        console.error("Hubo un error:", error);
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
          const modalData = await getEspecificCityData(
            this.origen,
            card.ciudad
          );
          console.log("Modal Data:", modalData);
          this.openModal(modalData);
          return;
        } catch (error) {
          console.error("Hubo un error:", error);
        } finally {
          this.loading = false;
          this.globalClicked = false;
        }
      }
    },
    selectOrigen(city) {
      console.log("origen", city);
      this.origen = city;
      this.citiesO = []; // Limpia las sugerencias después de seleccionar
    },
    selectDestino(city) {
      console.log("destino", city);
      this.destino = city;
      this.citiesD = []; // Limpia las sugerencias después de seleccionar
    },

    convertObjectToString(obj) {
      return Object.entries(obj)
        .map(([key, value]) => {
          if (Array.isArray(value)) {
            return `${key}: ${value.join(', ')}`;
          }
          return `${key}: ${value}`;
        })
        .join(' / ');
    },

    async saveInfo() {
      try {
        const user = JSON.parse(localStorage.getItem('user') || '{}');
        if (!user.id) {
          alert('No puede guardar información sin registrarse');
          this.router.push('/register');
          return;
        }
        console.log('Información a guardar:', this.selectedCard);
        const dataToSave = this.convertObjectToString(this.selectedCard);
        const newDetail = await apiPlaceCreate({
          especific_destination: dataToSave,
        })
        setTimeout(async () => {
          await fetchUserPlace(user.id, newDetail.id);
        }, 1000);

        alert('Información guardada con éxito');
        this.closeModal();
      } catch (error) {
        console.error('Error al guardar la información:', error);
        alert('Error al guardar la información');
      }
    },
    closeModal() {
      this.showModal = false;
    }
  },
};
</script>

<style scoped></style>
