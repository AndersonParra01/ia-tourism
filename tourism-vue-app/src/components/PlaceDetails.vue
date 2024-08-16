<template>
    <div class="p-8 bg-gray-50 min-h-screen">
        <h2 class="text-3xl font-bold mb-6 text-center text-blue-700">Información del Lugar</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Tarjeta de información principal -->
            <div class="bg-white shadow-md rounded-lg p-6" v-if="place">
                <h3 class="text-2xl font-semibold mb-2 text-green-700">{{ place.name }}</h3>
                <p class="text-gray-600 mb-4">{{ place.description }}</p>
                <div class="flex items-center mb-2">
                    <i class="fas fa-map-marker-alt text-red-500 mr-2"></i>
                    <span class="text-gray-700">{{ place.location }}</span>
                </div>
            </div>

            <!-- Tarjeta de comida típica -->
            <div class="bg-white shadow-md rounded-lg p-6" v-if="place.typical_food">
                <h3 class="text-xl font-semibold mb-2 text-orange-600">Comida Típica</h3>
                <p class="text-gray-600">{{ place.typical_food }}</p>
            </div>

            <!-- Tarjeta de música tradicional -->
            <div class="bg-white shadow-md rounded-lg p-6" v-if="place.traditional_music">
                <h3 class="text-xl font-semibold mb-2 text-purple-600">Música Tradicional</h3>
                <p class="text-gray-600">{{ place.traditional_music }}</p>
            </div>

            <!-- Tarjeta de idiomas -->
            <div class="bg-white shadow-md rounded-lg p-6" v-if="place.languages">
                <h3 class="text-xl font-semibold mb-2 text-blue-600">Idiomas</h3>
                <p class="text-gray-600">{{ place.languages }}</p>
            </div>

            <!-- Mapa turístico -->
            <div class="bg-white shadow-md rounded-lg p-6" v-if="place.city_tourist_map">
                <h3 class="text-xl font-semibold mb-2 text-green-600">Mapa Turístico</h3>
                <img :src="place.city_tourist_map" alt="Mapa turístico" class="rounded-lg shadow-sm">
            </div>

            <!-- Hoteles cercanos -->
            <div class="bg-white shadow-md rounded-lg p-6" v-if="place.hotels && place.hotels.length > 0">
                <h3 class="text-xl font-semibold mb-2 text-indigo-600">Hoteles Cercanos</h3>
                <ul class="list-disc list-inside text-gray-600">
                    <li v-for="hotel in place.hotels" :key="hotel">{{ hotel }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';

export default defineComponent({
    name: 'PlaceDetails',
    props: {
        place: {
            type: Object as PropType<{
                name: string;
                description: string;
                location: string;
                typical_food?: string;
                traditional_music?: string;
                languages?: string;
                city_tourist_map?: string;
                hotels?: string[];
            }>,
            required: true,
        },
    },
});
</script>

<style scoped></style>