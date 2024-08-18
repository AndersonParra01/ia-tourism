<template>
    <div class="p-8 bg-gray-50 min-h-screen">
        <h2 class="text-4xl font-bold mb-8 text-center text-blue-700">
            {{ message ? 'Respuesta del Asistente' : 'Información del Lugar' }}
        </h2>
        <div v-if="message"
            class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl">
            <h3 class="text-xl font-bold mb-4 text-red-600">Mensaje</h3>
            <p class="text-gray-700">{{ message }}</p>
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Tarjeta de información principal -->
            <div class="col-span-1 md:col-span-2 lg:col-span-3">
                <div tabindex="0"
                    class="collapse collapse-arrow bg-white shadow-lg rounded-xl transition-transform transform hover:scale-105 hover:shadow-xl">
                    <input type="checkbox" checked /> <!-- Aquí se agrega el atributo checked -->
                    <div class="collapse-title text-xl font-bold text-green-600">
                        Mapa Turístico e Imagen
                    </div>
                    <div class="collapse-content">
                        <div v-if="place.location" class="mb-4">
                            <img :src="place.location" alt="Mapa turístico"
                                class="rounded-lg shadow-md w-full h-64 object-cover" />
                        </div>
                    </div>
                </div>
            </div>
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

            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place.languages">
                <div>
                    <h3 class="text-xl font-bold mb-4 text-blue-600">Idiomas</h3>
                    <p class="text-gray-700">{{ place.languages }}</p>
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

            <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                v-if="place.regions">
                <div>
                    <h3 class="text-xl font-bold mb-4 text-green-600">Regiones Asociadas</h3>
                    <p class="text-gray-700">{{ place.regions }}</p>
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
import { fetchUserPlace } from "@/services/user";

export default defineComponent({
    name: "PlaceDetails",
    props: {
        place: {
            type: Object as PropType<{
                location: any;
                description_place: string;
                typical_food?: string;
                languages?: string;
                traditional_music?: string;
                city_tourist_map?: string;
                image?: string;
                hotels?: string;
                regions?: string;
            }>,
            required: true,
        },
        message: {
            type: String,
            default: null,
        },
    },
    methods: {
        async saveConsult() {
            const user = localStorage.getItem("user");
            if (!user) {
                alert("Debes iniciar sesión para guardar la consulta");
                return;
            }
            try {
                console.log('LUGAR', this.place);
                const newPlace = await apiPlaceCreate(this.place);
                console.log(newPlace);
                const user = JSON.parse(localStorage.getItem("user")!);
                const newUserPlace = await fetchUserPlace(user.id, newPlace.id);
                console.log('final', newUserPlace);
                alert("Guardado correctamente");
            } catch (error) {
                alert("Error al registrar historial");
                console.log(error);
                return;
            }
        },
    },
});
</script>

<style scoped>
/* Aquí puedes agregar estilos adicionales si es necesario */
</style>