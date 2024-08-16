<template>
    <div class="p-8 bg-gray-50 min-h-screen">
        <h2 class="text-4xl font-bold mb-8 text-center text-blue-700">Información del Lugar</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Tarjeta de información principal -->
            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place">
                <div>
                    <h3 class="text-2xl font-bold mb-4 text-green-800">Descripcion Lugar</h3>
                    <p class="text-gray-700">{{ place.description_place }}</p>
                </div>
                <div class="flex items-center mt-4">
                    <i class="fas fa-map-marker-alt text-red-500 mr-2"></i>
                    <!--  <span class="text-gray-800">{{ place.location }}</span> -->
                </div>
            </div>

            <!-- Tarjeta de comida típica -->
            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place.typical_food">
                <div>
                    <h3 class="text-xl font-bold mb-4 text-orange-600">Comida Típica</h3>
                    <p class="text-gray-700">{{ place.typical_food }}</p>
                </div>
            </div>

            <!-- Tarjeta de música tradicional -->
            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place.traditional_music">
                <div>
                    <h3 class="text-xl font-bold mb-4 text-purple-600">Música Tradicional</h3>
                    <p class="text-gray-700">{{ place.traditional_music }}</p>
                </div>
            </div>

            <!-- Tarjeta de idiomas -->
            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place.languages">
                <div>
                    <h3 class="text-xl font-bold mb-4 text-blue-600">Idiomas</h3>
                    <p class="text-gray-700">{{ place.languages }}</p>
                </div>
            </div>

            <!-- Acordeón para el mapa turístico y la imagen, ocupando toda la fila -->
            <div class="col-span-1 md:col-span-2 lg:col-span-3">
                <div tabindex="0"
                    class="collapse collapse-arrow bg-white shadow-lg rounded-xl transition-transform transform hover:scale-105 hover:shadow-xl">
                    <input type="checkbox" />
                    <div class="collapse-title text-xl font-bold text-green-600">
                        Mapa Turístico e Imagen
                    </div>
                    <div class="collapse-content">
                        <div v-if="place.city_tourist_map" class="mb-4">
                            <img :src="place.city_tourist_map" alt="Mapa turístico"
                                class="rounded-lg shadow-md w-full h-64 object-cover" />
                        </div>
                        <div v-if="place.image">
                            <img :src="place.image" alt="Imagen del lugar"
                                class="rounded-lg shadow-md w-full h-64 object-cover" />
                        </div>
                    </div>
                </div>
            </div>

            <!-- Hoteles cercanos -->
            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place.hotels && place.hotels.length > 0">
                <div>
                    <h3 class="text-xl font-bold mb-4 text-indigo-600">Hoteles Cercanos</h3>
                    <ul class="list-disc list-inside text-gray-700">
                        <li v-for="hotel in place.hotels" :key="hotel">{{ hotel }}</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="flex justify-center mt-10">
            <button @click="saveConsult"
                class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 px-6 rounded-lg shadow transition-all">
                Guardar Consulta
            </button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { apiPlaceCreate } from "@/services/place";

export default defineComponent({
    name: "PlaceDetails",
    props: {
        place: {
            type: Object as PropType<{
                description_place: string;
                typical_food?: string;
                languages?: string;
                traditional_music?: string;
                city_tourist_map?: string;
                image?: string;
                hotels?: string;
            }>,
            required: true,
        },
    },
    methods: {
        async saveConsult() {
            try {
                const newPlace = await apiPlaceCreate(this.place);
            } catch (error) {
                alert("Error al registrar historial");
                return;
            }
        },
    },
});
</script>

<style scoped>
/* Aquí puedes agregar estilos adicionales si es necesario */
</style>