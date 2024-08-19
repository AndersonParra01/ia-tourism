<template>
    <div class="p-8 bg-gray-50 min-h-screen">
        <div v-if="place">
            <h2 class="text-4xl font-bold mb-8 text-center text-blue-700">
                {{ message ? $t('assistantResponse') : $t('placeInformation') }}
            </h2>
            <div v-if="message"
                class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl">
                <h3 class="text-xl font-bold mb-4 text-red-600">{{ $t('message') }}</h3>
                <p class="text-gray-700">{{ message }}</p>
            </div>

            <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="col-span-1 md:col-span-2 lg:col-span-3">
                    <div tabindex="0"
                        class="collapse collapse-arrow bg-white shadow-lg rounded-xl transition-transform transform hover:scale-105 hover:shadow-xl">
                        <input type="checkbox" checked />
                        <div class="collapse-title text-xl font-bold text-green-600">
                            {{ $t('mapTouristImage') }} </div>
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
                        <h3 class="text-2xl font-bold mb-4 text-green-800">{{ $t('descriptionPlace') }}</h3>
                        <p class="text-gray-700">{{ place.description_place }}</p>
                    </div>
                    <div class="flex items-center mt-4">
                        <i class="fas fa-map-marker-alt text-red-500 mr-2"></i>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="place.typical_food">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-orange-600">{{ $t('typicalFood') }}</h3>
                        <p class="text-gray-700">{{ place.typical_food }}</p>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="place.languages">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-blue-600">{{ $t('languages') }}</h3>
                        <p class="text-gray-700">{{ place.languages }}</p>
                    </div>
                </div>



                <!-- Tarjeta de música tradicional -->
                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="place.traditional_music">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-purple-600">{{ $t('traditionalMusic') }}</h3>
                        <p class="text-gray-700">{{ place.traditional_music }}</p>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="place.regions">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-green-600">{{ $t('regions') }}</h3>
                        <p class="text-gray-700">{{ place.regions }}</p>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="place.hotels && place.hotels.length > 0">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-indigo-600"> {{ $t('hotelsNearby') }}</h3>
                        <ul class="list-disc list-inside text-gray-700">
                            <li v-for="hotel in place.hotels" :key="hotel">{{ hotel }}</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="flex justify-center mt-10">
                <button @click="saveConsult"
                    class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 px-6 rounded-lg shadow transition-all">
                    {{ $t('saveConsultation') }}
                </button>
            </div>
        </div>
        <div v-else>
            <h2 class="text-4xl font-bold mb-8 text-center text-blue-700">
                {{ message ? $t('assistantResponse') : $t('placeInformation') }}
            </h2>
            <div v-if="message"
                class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl">
                <h3 class="text-xl font-bold mb-4 text-red-600">{{ $t('message') }}</h3>
                <p class="text-gray-700">{{ message }}</p>
            </div>

            <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="col-span-1 md:col-span-2 lg:col-span-3">
                    <div tabindex="0"
                        class="collapse collapse-arrow bg-white shadow-lg rounded-xl transition-transform transform hover:scale-105 hover:shadow-xl">
                        <input type="checkbox" checked />
                        <div class="collapse-title text-xl font-bold text-green-600">
                            {{ $t('mapTouristImage') }} </div>
                        <div class="collapse-content">
                            <div v-if="placeById.location" class="mb-4">
                                <img :src="placeById.location" alt="Mapa turístico"
                                    class="rounded-lg shadow-md w-full h-64 object-cover" />
                            </div>
                        </div>
                    </div>
                </div>
                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="place">
                    <div>
                        <h3 class="text-2xl font-bold mb-4 text-green-800">{{ $t('descriptionPlace') }}</h3>
                        <p class="text-gray-700">{{ placeById.description_place }}</p>
                    </div>
                    <div class="flex items-center mt-4">
                        <i class="fas fa-map-marker-alt text-red-500 mr-2"></i>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="placeById.typical_food">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-orange-600">{{ $t('typicalFood') }}</h3>
                        <p class="text-gray-700">{{ placeById.typical_food }}</p>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="placeById.languages">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-blue-600">{{ $t('languages') }}</h3>
                        <p class="text-gray-700">{{ placeById.languages }}</p>
                    </div>
                </div>



                <!-- Tarjeta de música tradicional -->
                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="placeById.traditional_music">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-purple-600">{{ $t('traditionalMusic') }}</h3>
                        <p class="text-gray-700">{{ placeById.traditional_music }}</p>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="placeById.regions">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-green-600">{{ $t('regions') }}</h3>
                        <p class="text-gray-700">{{ placeById.regions }}</p>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl p-8 flex flex-col justify-between h-full transition-transform transform hover:scale-105 hover:shadow-xl"
                    v-if="placeById.hotels && placeById.hotels.length > 0">
                    <div>
                        <h3 class="text-xl font-bold mb-4 text-indigo-600"> {{ $t('hotelsNearby') }}</h3>
                        <ul class="list-disc list-inside text-gray-700">
                            <li v-for="hotel in placeById.hotels" :key="hotel">{{ hotel }}</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="flex justify-center mt-10">
                <button @click="returnHistory"
                    class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 px-6 rounded-lg shadow transition-all">
                    {{ $t('exit') }}
                </button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, PropType, ref, watch } from "vue";
import { apiPlaceById, apiPlaceCreate } from "@/services/place";
import { fetchUserPlace } from "@/services/user";
import { useRoute } from 'vue-router';

export default defineComponent({
    setup(props) {
        const route = useRoute();
        const placeId = ref<number | null>(null);
        const placeById = ref({
            id: null,
            location: null,
            description_place: "",
            typical_food: "",
            languages: "",
            traditional_music: "",
            city_tourist_map: "",
            image: "",
            hotels: "",
            regions: ""
        });
        const fetchPlaceDataById = async (id: number) => {
            try {
                const data = await apiPlaceById(id);
                placeById.value = data;
                console.log('BY ID', data);
            } catch (error) {
                console.error("Error fetching place details:", error);
            }
        };
        onMounted(() => {
            placeId.value = parseInt(route.params.id as string, 10);
            console.log('ID capturado:', placeId.value);

            if (placeId.value) {
                fetchPlaceDataById(placeId.value);
            }
        });
        return {
            fetchPlaceDataById,
            placeById
        };
    },
    name: "PlaceDetails",
    props: {
        place: {
            type: Object as PropType<{
                id?: number;
                location?: any;
                description_place?: string;
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
                window.location.reload();
            } catch (error) {
                alert("Error al registrar historial");
                console.log(error);
                return;
            }
        },
        returnHistory() {
            console.log('Regresar al historial');
            this.$router.push("/historial-busquedas");
        },
    },

});
</script>

<style scoped></style>