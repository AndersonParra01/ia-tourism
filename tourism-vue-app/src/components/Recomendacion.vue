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
          <option v-for="option in options" :key="option" :value="option">{{ option }}</option>
        </select>
      </div>
      <button @click="getPlaces"
        class="w-full px-4 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-200">
        {{ $t('searchButton') }}
      </button>
    </div>

    <div v-if="loading" class="text-center text-gray-600 mt-4">
      {{ $t('loading') }}
    </div>
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-8 w-full max-w-5xl">
      <div v-for="card in cards" :key="card.ciudad"
        class="bg-white p-6 rounded-lg shadow hover:shadow-lg transition duration-200 cursor-pointer"
        @click="getPlaceFromRecommendation(card)" :class="{ disabled: globalClicked }">
        <h3 class="text-xl font-semibold text-gray-800 mb-2">{{ card.ciudad }}</h3>
        <p class="text-gray-600">{{ $t('expense') }}: {{ card.gasto }}</p>
        <p class="text-gray-600">{{ $t('time') }}: {{ card.tiempo }}</p>
        <p class="text-gray-600">{{ card.descripcion }}</p>
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

        <h3 class="text-2xl font-bold mb-4 text-gray-800 text-center">{{ selectedCard.ciudad }}</h3>

        <div class="grid grid-cols-1 md:grid-cols-2  space-y-4">
          <div v-if="selectedCard.transporte">
            <p class="text-gray-700 strong ">
              <strong>
                {{ $t('details.transportExpense') }}
              </strong>
            </p>
            <ul class="list-disc list-inside text-gray-700 pl-4">
              <li v-for="item in selectedCard.transporte" :key="item">{{ item }}</li>
            </ul>
          </div>

          <p v-if="selectedCard.hotel" class="text-gray-700"><b>{{ $t('details.lodgingExpense') }}</b> {{
            selectedCard.hotel }}</p>
          <p v-if="selectedCard.comida" class="text-gray-700"><b>{{ $t('details.foodExpense') }}</b> {{
            selectedCard.comida }}</p>
          <p v-if="selectedCard.documentacion" class="text-gray-700"><b>{{ $t('details.documentation') }}</b> {{
            selectedCard.documentacion }}</p>
          <p v-if="selectedCard.duracion" class="text-gray-700"><b>{{ $t('details.tripDuration') }}</b> {{
            selectedCard.duracion }}</p>
          <p v-if="selectedCard.descripcion" class="text-gray-700"><b>{{ $t('description') }}</b> {{
            selectedCard.descripcion }}</p>
          <p v-if="selectedCard.lugares" class="text-gray-700"><b>{{ $t('details.places') }}</b> {{
            selectedCard.lugares.join(', ') }}</p>
          <p v-if="selectedCard.transp_local" class="text-gray-700"><b>{{ $t('details.localTransport') }}</b> {{
            selectedCard.transp_local }}</p>
          <p v-if="selectedCard.clima" class="text-gray-700"><b>{{ $t('details.climate') }}</b> {{ selectedCard.clima }}
          </p>
          <p v-if="selectedCard.seguridad" class="text-gray-700"><b>{{ $t('details.security') }}</b> {{
            selectedCard.seguridad }}</p>
          <p v-if="selectedCard.idioma" class="text-gray-700"><b>{{ $t('details.language') }}</b> {{ selectedCard.idioma
            }}</p>
          <p v-if="selectedCard.moneda" class="text-gray-700"><b>{{ $t('details.currency') }}</b> {{ selectedCard.moneda
            }}</p>
          <p v-if="selectedCard.costumbres" class="text-gray-700"><b>{{ $t('details.customs') }}</b> {{
            selectedCard.costumbres }}</p>
          <p v-if="selectedCard.gastronomia" class="text-gray-700"><b>{{ $t('details.gastronomy') }}</b> {{
            selectedCard.gastronomia }}</p>
          <p v-if="selectedCard.cultura" class="text-gray-700"><b>{{ $t('details.culture') }}</b> {{
            selectedCard.cultura }}</p>
          <p v-if="selectedCard.historia" class="text-gray-700"><b>{{ $t('details.history') }}</b> {{
            selectedCard.historia }}</p>
          <p v-if="selectedCard.turismo" class="text-gray-700"><b>{{ $t('details.tourism') }}</b> {{
            selectedCard.turismo }}</p>
          <p v-if="selectedCard.compras" class="text-gray-700"><b>{{ $t('details.shopping') }}</b> {{
            selectedCard.compras }}</p>
          <p v-if="selectedCard.vida_nocturna" class="text-gray-700"><b>{{ $t('details.nightlife') }}</b> {{
            selectedCard.vida_nocturna }}</p>
          <p v-if="selectedCard.transporte_local" class="text-gray-700"><b>{{ $t('details.localTransportDetails') }}</b>
            {{ selectedCard.transporte_local }}</p>
          <p v-if="selectedCard.alojamiento" class="text-gray-700"><b>{{ $t('details.accommodation') }}</b> {{
            selectedCard.alojamiento }}</p>
          <p v-if="selectedCard.restaurantes" class="text-gray-700"><b>{{ $t('details.restaurants') }}</b> {{
            selectedCard.restaurantes }}</p>
          <p v-if="selectedCard.actividades" class="text-gray-700"><b>{{ $t('details.activities') }}</b> {{
            selectedCard.actividades }}</p>
          <p v-if="selectedCard.consejos" class="text-gray-700"><b>{{ $t('details.tips') }}</b> {{ selectedCard.consejos
            }}</p>
          <p v-if="selectedCard.emergencias" class="text-gray-700"><b>{{ $t('details.emergencies') }}</b> {{
            selectedCard.emergencias }}</p>
          <p v-if="selectedCard.telefono" class="text-gray-700"><b>{{ $t('details.phone') }}</b> {{
            selectedCard.telefono }}</p>
          <p v-if="selectedCard.salud" class="text-gray-700"><b>{{ $t('details.health') }}</b> {{ selectedCard.salud }}
          </p>
          <p v-if="selectedCard.seguro" class="text-gray-700"><b>{{ $t('details.insurance') }}</b> {{
            selectedCard.seguro }}</p>
          <p v-if="selectedCard.comunicacion" class="text-gray-700"><b>{{ $t('details.communication') }}</b> {{
            selectedCard.comunicacion }}</p>
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

<style scoped></style>
