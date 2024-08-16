<template>
    <div class="mt-2 p-8 bg-white shadow-md rounded-lg">
        <h1 class="text-3xl font-bold mb-6 text-center text-blue-700">
            OpenAI Asistente de Turismo Virtual Ec
        </h1>
        <div class="mb-6 text-center">
            <label for="language" class="text-lg font-semibold text-gray-700">Seleccione su idioma:</label>
            <select v-model="language" id="language" class="ml-2 p-2 border rounded bg-gray-50">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
            </select>
        </div>
        <div class="flex justify-center items-center mb-4">
            <input v-model="prompt" type="text" placeholder="Selecciona tu lugar turistico"
                class="border border-gray-300 rounded-l p-3 w-full max-w-md" @keydown.enter="send" />
            <button @click="send" class="bg-blue-500 hover:bg-blue-600 text-white p-3 rounded-r">
                Enviar
            </button>
        </div>

        <div v-if="isLoading" class="flex space-x-4 mt-4">
            <WaitComponent />
        </div>

        <PlaceDetails v-if="isDataReady" :place="selectedPlace" />

        <!-- <Map /> -->


    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { getCompletion, Place } from "./../services/ia";
import DynamicText from "./DynamicText.vue";
import WaitComponent from "./wait.vue";
import Map from "./Map.vue";
import { apiRegister } from "@/services/auth";
import PlaceDetails from './PlaceDetails.vue';

export default defineComponent({
    setup() {
        const prompt = ref("");
        const response = ref("");
        const isLoading = ref(false);
        const message = ref("");
        const message2 = ref("");
        let language: "en" | "es" | "fr" = "en";
        const isDataReady = ref(false)
        const selectedPlace = ref<Place>({
            description_place: '',
            image: '',
            typical_food: "",
            languages: "",
            traditional_music: "",
            city_tourist_map: "",
            map_of_tourist_places_in_ecuador: "",
            hotels: "",
            regions: "",
        });
        const send = async () => {
            try {
                isLoading.value = true;
                const result: Place = await getCompletion(prompt.value);
                console.log('XD', result);

                selectedPlace.value = result;
                isLoading.value = false;
                isDataReady.value = true;
            } catch (error) {
                isLoading.value = false;
                console.error("Error fetching completion:", error);
                isDataReady.value = false;
            }
        };
        return { prompt, response, send, language, message, message2, isLoading, selectedPlace, isDataReady };
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
        PlaceDetails
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
                alert('Error al registrar usuario');
                return;
            }

            const placeObject = JSON.parse(localStorage.getItem("place") || "");
            window.location.reload();
        },

    },
});
</script>

<style>
.modal-bg {
    background-color: rgba(0, 0, 0, 0.75);
}

.abs-center {
    display: flex;
    align-items: center;
    justify-content: center;
}

form {
    text-align: center;
    margin: auto;
    width: 50%;
    max-width: 325px;
    min-width: 325px;
    padding: 0 30px 30px 30px;
    opacity: 0.85;
    box-shadow: 0px 0px 10px rgb(6, 7, 45), 0px 0px 30px white;
}

.form-control {
    display: block;
    padding: 10px;
    width: 100%;
    margin: 5px 0;
    font-size: 18px;
    margin-bottom: 5px;
    border-radius: 5px;
    height: 35px;
    border: 1px solid #6b6767;
}

.btn {
    width: 100%;
    margin-bottom: 15px;
    height: 35px;
    border-radius: 10px;
}

.imagenUsuario {
    margin-top: -50px;
    margin-bottom: 35px;
}

.imagenUsuario img {
    width: 100px;
    height: 100px;
    box-shadow: 0px 0px 3px #848484;
    border-radius: 50%;
    margin-left: auto;
    margin-right: auto;
}
</style>
