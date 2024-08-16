<template>
    <div class="container">
      <!-- Campos de Texto -->
      <div class="autocomplete-container">
        <div>
          <input v-model="origen" @input="fetchCitiesO" placeholder="Origen" autocomplete="off"/>
          <!-- Lista de Sugerencias -->
          <ul v-if="citiesO.length" class="autocomplete-list">
            <li v-for="(city, index) in citiesO" :key="index" @click="selectOrigen(city)">
              {{ city }}
            </li>
          </ul>
        </div>
        <div>
          <input v-model="destino" @input="fetchCitiesD" placeholder="Destino" autocomplete="off"/>
          <!-- Lista de Sugerencias -->
          <ul v-if="citiesD.length" class="autocomplete-list">
            <li v-for="(city, index) in citiesD" :key="index" @click="selectDestino(city)">
              {{ city }}
            </li>
          </ul>
        </div>
        <button @click="getPlaces" class="styled-button">Buscar</button>
      </div>
  
      <!-- Combo -->
      <div class="select-container">
        <select v-model="selectedOption">
          <option v-for="option in options" :key="option" :value="option">{{ option }}</option>
        </select>
      </div>
  
      <!-- Cards Dinámicas -->
      <div v-if="loading">Cargando...</div>
      <div v-else class="cards-container">
        <div v-for="card in cards" :key="card.ciudad" class="card" @click="openModal(card)">
          <h3>{{ card.ciudad }}</h3>
          <p>Gasto: {{ card.gasto }}</p>
          <p>Tiempo: {{ card.tiempo }}</p>
          <p>{{ card.descripcion }}</p>
        </div>
      </div>

      <div v-if="showModal" class="modal" @click="handleClickOutside">
        <div class="modal-content" @click.stop>
          <button class="close" @click="closeModal">&times;</button>
          <h3>{{ selectedCard.ciudad }}</h3>
          <div class="details">
            <div v-if="selectedCard.transporte">
              <p><b>Gasto en transporte: </b></p>
              <ul>
                <li v-for="item in selectedCard.transporte" :key="item">{{ item }}</li>
              </ul>
            </div>
            <p v-if="selectedCard.hotel"><b>Gastos Hospedaje:</b> {{ selectedCard.hotel }}</p>
            <p v-if="selectedCard.comida"><b>Gasto en comidas:</b> {{ selectedCard.comida }}</p>
            <p v-if="selectedCard.documentacion"><b>Documentación necesaria:</b> {{ selectedCard.documentacion }}</p>
            <p v-if="selectedCard.duracion"><b>Duración de viaje:</b> {{ selectedCard.duracion }}</p>
            <p v-if="selectedCard.descripcion"><b>Descripción:</b> {{ selectedCard.descripcion }}</p>
            <p v-if="selectedCard.lugares"><b>Lugares:</b> {{ selectedCard.lugares.join(', ') }}</p>
            <p v-if="selectedCard.transp_local"><b>Transporte Local:</b> {{ selectedCard.transp_local }}</p>
            <p v-if="selectedCard.clima"><b>Clima:</b> {{ selectedCard.clima }}</p>
            <p v-if="selectedCard.seguridad"><b>Seguridad:</b> {{ selectedCard.seguridad }}</p>
            <p v-if="selectedCard.idioma"><b>Idioma:</b> {{ selectedCard.idioma }}</p>
            <p v-if="selectedCard.moneda"><b>Moneda:</b> {{ selectedCard.moneda }}</p>
            <p v-if="selectedCard.costumbres"><b>Costumbres:</b> {{ selectedCard.costumbres }}</p>
            <p v-if="selectedCard.gastronomia"><b>Gastronomía:</b> {{ selectedCard.gastronomia }}</p>
            <p v-if="selectedCard.cultura"><b>Cultura:</b> {{ selectedCard.cultura }}</p>
            <p v-if="selectedCard.historia"><b>Historia:</b> {{ selectedCard.historia }}</p>
            <p v-if="selectedCard.turismo"><b>Turismo:</b> {{ selectedCard.turismo }}</p>
            <p v-if="selectedCard.compras"><b>Compras:</b> {{ selectedCard.compras }}</p>
            <p v-if="selectedCard.vida_nocturna"><b>Vida Nocturna:</b> {{ selectedCard.vida_nocturna }}</p>
            <p v-if="selectedCard.transporte_local">Transporte <b>Local:</b> {{ selectedCard.transporte_local }}</p>
            <p v-if="selectedCard.alojamiento"><b>Alojamiento:</b> {{ selectedCard.alojamiento }}</p>
            <p v-if="selectedCard.restaurantes"><b>Restaurantes:</b> {{ selectedCard.restaurantes }}</p>
            <p v-if="selectedCard.actividades"><b>Actividades:</b> {{ selectedCard.actividades }}</p>
            <p v-if="selectedCard.consejos"><b>Consejos:</b> {{ selectedCard.consejos }}</p>
            <p v-if="selectedCard.emergencias"><b>Emergencias:</b> {{ selectedCard.emergencias }}</p>
            <p v-if="selectedCard.telefono"><b>Teléfono:</b> {{ selectedCard.telefono }}</p>
            <p v-if="selectedCard.salud"><b>Salud:</b> {{ selectedCard.salud }}</p>
            <p v-if="selectedCard.seguro"><b>Seguro:</b> {{ selectedCard.seguro }}</p>
            <p v-if="selectedCard.comunicacion"><b>Comunicación:</b> {{ selectedCard.comunicacion }}</p>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script>
  import { getTouristPlaces, getEspecificCityData, fetchCities } from '../services/ia';

  export default {
    data() {
      return  {
        origen: '',
        destino: '',
        selectedOption: 'General',
        options: ['General', 'Economico', 'Historico', 'Cultural', 'Diversión', 'Internacional'],
        touristPlaces: [],
        card: [],
        loading: false,
        showModal: false,
        selectedCard: {},
        citiesO: [],
        citiesD: [],
      };
    },
    methods: {
        openModal(card) {
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
              if(this.origen === '') {
                alert('Por favor, ingrese un origen');
                return;
              }

              if(this.origen !== '' && this.destino !== '') {
                console.log('Destino:', this.destino);
                const modalData = await getEspecificCityData(this.origen, this.destino);
                this.openModal(modalData);
                return;
              }

              const places = await getTouristPlaces(this.origen);
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
        selectOrigen(city) {
          console.log('origen',city);
          this.origen = city;
          this.citiesO = []; // Limpia las sugerencias después de seleccionar
        },
        selectDestino(city) {
          console.log('destino',city);
          this.destino = city;
          this.citiesD = []; // Limpia las sugerencias después de seleccionar
        },
    },
  };
</script>
  
<style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start; /* Cambiado de center a flex-start para alinear al inicio verticalmente */
    min-height: 200vh;
    gap: 30px;
    background-color: #f0f0f0;
    padding: 100px;
  }
  
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
    background-color: #007BFF; /* Primary blue color */
    color: white; /* White text */
    border: none; /* Remove default border */
    padding: 10px 20px; /* Add some padding */
    font-size: 16px; /* Increase font size */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background-color 0.3s ease; /* Smooth transition for background color */
    height: 45px;
    margin-left: 15px;
  }

  .styled-button:hover {
    background-color: #0056b3; /* Darker blue on hover */
  }

  .modal {
  display: flex; /* Asegúrate de que esté visible */
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1000; /* Aumenta el z-index para que esté encima de otros elementos */
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
  opacity: 1; /* Asegura la opacidad */
  transition: opacity 0.3s ease-in-out; /* Transición suave */
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
    opacity: 1; /* Asegura la opacidad */
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
    width: 45%; /* Ancho del contenedor del input */
  }

  input {
    padding: 10px;
    border-radius: 8px;
    border: 2px solid #ccc;
    font-size: 1.1em;
    width: 100%; /* El input ocupa todo el ancho del contenedor */
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
  