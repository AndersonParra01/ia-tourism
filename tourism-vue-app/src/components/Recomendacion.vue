<template>
    <div class="container">
      <!-- Campos de Texto -->
      <div class="input-container">
        <input v-model="origen" placeholder="Origen" />
        <input v-model="destino" placeholder="Destino" />
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

      <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h3>{{ selectedCard.ciudad }}</h3>
        <div class="details">
          <div>
            <p v-if="selectedCard.gasto">Gastos:</p>
            <div v-if="selectedCard.gasto">
              <div v-for="(value, key) in selectedCard.gasto" :key="key">
                <p>{{ key }}:</p>
                <ul v-if="Array.isArray(value)">
                  <li v-for="item in value" :key="item">{{ item }}</li>
                </ul>
                <p v-else>{{ value }}</p>
              </div>
            </div>
          </div>
          <p v-if="selectedCard.duracion">Duración: {{ selectedCard.duracion }}</p>
          <p v-if="selectedCard.descripcion">Descripción: {{ selectedCard.descripcion }}</p>
          <p v-if="selectedCard.lugares">Lugares: {{ selectedCard.lugares.join(', ') }}</p>
          <p v-if="selectedCard.transporte">Transporte: {{ selectedCard.transporte }}</p>
          <p v-if="selectedCard.clima">Clima: {{ selectedCard.clima }}</p>
          <p v-if="selectedCard.seguridad">Seguridad: {{ selectedCard.seguridad }}</p>
          <p v-if="selectedCard.idioma">Idioma: {{ selectedCard.idioma }}</p>
          <p v-if="selectedCard.moneda">Moneda: {{ selectedCard.moneda }}</p>
          <p v-if="selectedCard.costumbres">Costumbres: {{ selectedCard.costumbres }}</p>
          <p v-if="selectedCard.gastronomia">Gastronomía: {{ selectedCard.gastronomia }}</p>
          <p v-if="selectedCard.cultura">Cultura: {{ selectedCard.cultura }}</p>
          <p v-if="selectedCard.historia">Historia: {{ selectedCard.historia }}</p>
          <p v-if="selectedCard.turismo">Turismo: {{ selectedCard.turismo }}</p>
          <p v-if="selectedCard.compras">Compras: {{ selectedCard.compras }}</p>
          <p v-if="selectedCard.vida_nocturna">Vida Nocturna: {{ selectedCard.vida_nocturna }}</p>
          <p v-if="selectedCard.transporte_local">Transporte Local: {{ selectedCard.transporte_local }}</p>
          <p v-if="selectedCard.alojamiento">Alojamiento: {{ selectedCard.alojamiento }}</p>
          <p v-if="selectedCard.restaurantes">Restaurantes: {{ selectedCard.restaurantes }}</p>
          <p v-if="selectedCard.actividades">Actividades: {{ selectedCard.actividades }}</p>
          <p v-if="selectedCard.consejos">Consejos: {{ selectedCard.consejos }}</p>
          <p v-if="selectedCard.emergencias">Emergencias: {{ selectedCard.emergencias }}</p>
          <p v-if="selectedCard.telefono">Teléfono: {{ selectedCard.telefono }}</p>
          <p v-if="selectedCard.salud">Salud: {{ selectedCard.salud }}</p>
          <p v-if="selectedCard.seguro">Seguro: {{ selectedCard.seguro }}</p>
          <p v-if="selectedCard.comunicacion">Comunicación: {{ selectedCard.comunicacion }}</p>
        </div>
      </div>
    </div>
    </div>
  </template>
  
  <script>
  import { getTouristPlaces, getEspecificCityData } from '../services/ia';

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
        selectedCard: {}
      };
    },
    methods: {
        openModal(card) {
          this.selectedCard = card;
          this.showModal = true;
        },
        closeModal() {
          this.showModal = false;
        },
        async getPlaces() {  
          this.loading = true;     
            try {
              if(this.origen === '') {
                alert('Por favor, ingrese un origen');
                return;
              }

              if(this.origen !== '' && this.destino !== '') {
                const modalData = await getEspecificCityData(this.origen, this.destino);
                this.openModal(modalData);
                return;
              }

              const places = await getTouristPlaces(this.origen);
              this.cards = places;
            } catch (error) {
                console.error('Error al obtener datos de la API:', error);
            } finally {
                this.loading = false;
            }
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
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
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
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
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
  </style>
  