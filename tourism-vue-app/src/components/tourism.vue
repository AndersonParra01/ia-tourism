<template>
    <div class="mt-2 p-8 bg-white shadow-md rounded-lg">
        <h1 class="text-3xl font-bold mb-6 text-center text-blue-700">
            OpenAI Asistente de Turismo Virtual Ec
        </h1>
        <div class="flex justify-center mb-6">
            <button @click="setActiveTab('general')" :class="tabClasses('general')"
                class="px-6 py-2 font-semibold rounded-l-lg transition-colors duration-300">
                Búsqueda General
            </button>
            <button @click="setActiveTab('favorites')" :class="tabClasses('favorites')"
                class="px-6 py-2 font-semibold rounded-r-lg transition-colors duration-300">
                Buscar Destinos Favoritos
            </button>
        </div>

        <div v-if="activeTab === 'general'" class="flex justify-center items-center mb-4 p-4">
            <input v-model="prompt" type="text" placeholder="Selecciona tu lugar turístico"
                class="border border-gray-300 rounded-l p-3 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                @keydown.enter="send" />
            <button @click="send"
                class="bg-blue-500 hover:bg-blue-600 text-white p-3 rounded-r transition-colors duration-300">
                Enviar
            </button>
            <button @click="startRecognition"
                class="ml-2 bg-gray-500 hover:bg-gray-600 text-white p-3 rounded transition-colors duration-300">
                🎤
            </button>
        </div>

        <div v-if="activeTab === 'favorites'" class="text-center text-gray-600">
            <Recomendacion />
        </div>

        <div v-if="isLoading" class="flex space-x-4 mt-4">
            <WaitComponent />
        </div>

        <PlaceDetails v-if="isDataReady" :place="selectedPlace" />
    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref, watch } from "vue";
import { getCompletion, Place } from "./../services/ia";
import DynamicText from "./DynamicText.vue";
import WaitComponent from "./wait.vue";
import Map from "./Map.vue";
import { apiRegister } from "@/services/auth";
import PlaceDetails from "./PlaceDetails.vue";
import { useSpeechRecognition } from "@vueuse/core";
import Recomendacion from "./Recomendacion.vue";
export default defineComponent({
    setup() {
        const prompt = ref("");
        const response = ref("");
        const isLoading = ref(false);
        const language: "en" | "es" | "fr" = "es";
        const isDataReady = ref(false);
        const selectedPlace = ref<Place>({
            description_place: "",
            image: "",
            typical_food: "",
            languages: "",
            traditional_music: "",
            city_tourist_map: "",
            map_of_tourist_places_in_ecuador: "",
            hotels: "",
            regions: "",
            location: ""
        });
        const imageFile = ref<File>(new File([], ''));
        const activeTab = ref<'general' | 'favorites'>('general');
        const message = ref<string | null>(null);

        onMounted(() => {
            const savedTab = localStorage.getItem('activeTab') as 'general' | 'favorites';
            if (savedTab) {
                activeTab.value = savedTab;
            }
        });

        const setActiveTab = (tab: 'general' | 'favorites') => {
            isDataReady.value = false;
            prompt.value = '';
            activeTab.value = tab;
            localStorage.setItem('activeTab', tab);
        };

        const tabClasses = (tab: 'general' | 'favorites') => {
            return activeTab.value === tab
                ? 'bg-blue-500 text-white'
                : 'bg-gray-200 text-gray-700';
        };

        const send = async () => {
            try {
                isDataReady.value = false;
                isLoading.value = true;
                const result: Place = await getCompletion(prompt.value, language, imageFile.value || null);
                console.log("XD", result);

                selectedPlace.value = result;
                isLoading.value = false;
                isDataReady.value = true;
            } catch (error) {
                isLoading.value = false;
                console.error("Error fetching completion:", error);
                isDataReady.value = false;
            }
        };

        const { isListening, result, start, stop } = useSpeechRecognition({
            lang: language,
            interimResults: true,
            continuous: true,
        });

        let silenceTimer: number | null = null;

        watch(result, (newResult) => {
            console.log('TEMPORIZADOR', result.value);
            if (newResult) {
                prompt.value = newResult;
                if (silenceTimer) {
                    clearTimeout(silenceTimer);
                }

                silenceTimer = setTimeout(() => {
                    stop();
                    if (prompt.value === '') {
                        alert('No se ha detectado ningun mensaje');
                    }
                    send();
                }, 2000);
            }
        });

        const startRecognition = () => {
            start();
            silenceTimer = setTimeout(() => {
                stop();
            }, 5000);
        };

        const stopRecognition = () => {
            stop();
        };

        const handleImageUpload = (event: Event) => {
            /* const input = event.target as HTMLInputElement;
            if (input.files && input.files.length > 0) {
              imageFile.value = input.files[0];
            } */
        };
        return {
            prompt,
            response,
            send,
            language,
            message,
            isLoading,
            selectedPlace,
            isDataReady,
            handleImageUpload,
            startRecognition,
            stopRecognition,
            isListening,
            setActiveTab,
            activeTab,
            tabClasses
        };
    },
    computed: {
        isUserLoggedIn() {
            if (typeof localStorage !== "undefined") {
                return localStorage.getItem("user") !== null;
            }
            return false;
        },
    },
    components: {
        DynamicText,
        Map,
        WaitComponent,
        PlaceDetails,
        Recomendacion
    },
    data() {
        return {
            isModalOpen: false,
            name: "",
            lastName: "",
            username: "",
            password: "",
            confirmPassword: "",
        };
    },
    methods: {
        openModal() {
            this.isModalOpen = true;
        },
        closeModal() {
            this.isModalOpen = false;
        },
        async submitForm() {
            if (localStorage.getItem("place") === null) {
                alert("Primero debe enviar la consulta");
                return;
            }

            if (this.password !== this.confirmPassword) {
                alert("Las contraseñas no coinciden");
                return;
            }

            try {
                const user = {
                    names: this.name,
                    lastnames: this.lastName,
                    username: this.username,
                    password: this.password,
                };
                const result = await apiRegister(user);
                localStorage.setItem("user", JSON.stringify(result));
            } catch (error) {
                alert("Error al registrar usuario");
                return;
            }

            const placeObject = JSON.parse(localStorage.getItem("place") || "");
            window.location.reload();
        },
    },
});
</script>

<style></style>
