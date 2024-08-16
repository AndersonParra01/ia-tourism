<template>
    <div class="m-4 mx-auto p-3">
        <h1 class="text-2xl font-bold mb-4">
            OpenAI Asistente de Turismo Virtual Ec
        </h1>
        <div>
            <label for="language">Seleccione su idioma:</label>
            <select v-model="language" id="language">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
            </select>
        </div>
        <input v-model="prompt" type="text" placeholder="Enter a prompt" class="border rounded p-2 mb-4 w-full" />
        <button @click="send" class="bg-blue-500 text-white p-2 rounded">
            Enviar
        </button>
        <p class="mt-4">{{ response }}</p>

        <h3></h3>

        <div class="flex space-x-4 mt-4">
            <DynamicText :text="message" class="flex-1" />
            <DynamicText :text="message2" class="flex-1" />
            <DynamicText :text="message" class="flex-1" />
            <DynamicText :text="message2" class="flex-1" />
            <DynamicText :text="message2" class="flex-1" />
        </div>
        <Map />
        <div v-if="isUserLoggedIn">
            <button @click="saveConsult" class="bg-blue-500 text-white p-2 rounded">
                Guardar Consulta
            </button>
        </div>

        <div id="app" v-else>
            <!-- Botón para abrir el modal -->
            <button @click="openModal" class="bg-blue-500 text-white py-2 px-4 rounded">
                Registrarse para guardar Información
            </button>

            <!-- Modal -->
            <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-75">
                <div class="bg-white p-6 rounded shadow-lg w-full max-w-md">
                    <!-- Botón para cerrar el modal -->
                    <button @click="closeModal" class="text-gray-500 hover:text-gray-700 float-right">
                        &times;
                    </button>

                    <!-- Formulario dentro del modal -->
                    <div class="abs-center">
                        <form @submit.prevent="submitForm">
                            <div class="imagenUsuario">
                                <img
                                    src="data:image/png;base64,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" />
                            </div>
                            <label for="name" style="font-weight: bold">Nombre:</label>
                            <input v-model="name" type="text" name="name" id="name" class="form-control"
                                placeholder="Nombre" required />
                            <label for="lastName" style="font-weight: bold">Apellido:</label>
                            <input v-model="lastName" type="text" name="lastName" id="lastName" class="form-control"
                                placeholder="Apellido" required />
                            <label for="username" style="font-weight: bold">Usuario:</label>
                            <input v-model="username" type="text" name="username" id="username" class="form-control"
                                placeholder="Usuario" required />
                            <label for="password" style="font-weight: bold">Password:</label>
                            <input v-model="password" type="password" name="password" id="password" class="form-control"
                                placeholder="Password" required />
                            <label for="confirmPassword" style="font-weight: bold">Confirmar Password:</label>
                            <input v-model="confirmPassword" type="password" name="confirmPassword" id="confirmPassword"
                                class="form-control" placeholder="Confirmar Password" required />
                            <button type="submit"
                                class="w-full my-4 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">Registrar</button>
                            <button type="button" @click="closeModal"
                                class="w-full my-4 bg-transparent hover:bg-red-500 text-red-700 font-semibold hover:text-white py-2 px-4 border border-red-500 hover:border-transparent rounded">
                                Cancelar
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { getCompletion, Place } from "./../services/ia";
import DynamicText from "./DynamicText.vue";
import Map from "./Map.vue";
import { apiRegister } from "@/services/auth";
import { apiPlaceCreate } from "@/services/place";

export default defineComponent({
    setup() {
        const prompt = ref("");
        const response = ref("");
        const isLoading = ref(false);
        const message = ref("");
        const message2 = ref("");
        let language: "en" | "es" | "fr" = "en";

        /* const send = async () => {
            try {
                isLoading.value = true;
                message2.value = "Cargando... enviado";
                message.value = "Cargando... enviado1";
                // const result = await getCompletion(prompt.value);

                //OBJETO A CREAR DEPENDIENDO DE LA RESPUESTA
                const result = {
                    name: "Great Wall of China",
                    description: "One of the greatest wonders of the world.",
                    image: "great-wall-image-url",
                    location: "China",
                    users: [1]
                }
                localStorage.setItem("place", JSON.stringify(result));
                isLoading.value = false;
            } catch (error) {
                isLoading.value = false;
                console.error("Error fetching completion:", error);
            }
        }; */
        const send = async () => {
            try {
                isLoading.value = true;
                message2.value = "Cargando... enviado";
                message.value = "Cargando... enviado1";

                // Utilizamos la función getCompletion del servicio
                const result: Place = await getCompletion(prompt.value);

                console.log('XD', result);
                // Guarda el resultado en el localStorage
                localStorage.setItem("place", JSON.stringify(result));

                isLoading.value = false;
            } catch (error) {
                isLoading.value = false;
                console.error("Error fetching completion:", error);
            }
        };
        return { prompt, response, send, language, message, message2 };
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
        Map
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
            const place = await apiPlaceCreate(placeObject);
            localStorage.removeItem("place");

            // this.closeModal(); // Cierra el modal después de enviar el formulario
            window.location.reload();
        },
        async saveConsult() {
            try {
                if (localStorage.getItem("place") === null) {
                    alert("Primero debe enviar la consulta");
                    return;
                }
                const placeObject = JSON.parse(localStorage.getItem("place") || "");
                const place = await apiPlaceCreate(placeObject);
                localStorage.removeItem("place");
            } catch (error) {
                alert('Error al registrar historial');
                return;
            }
        }
    },
});
</script>

<style>
/* Estilos adicionales */
.modal-bg {
    background-color: rgba(0, 0, 0, 0.75);
    /* Fondo más opaco */
}

.abs-center {
    display: flex;
    align-items: center;
    justify-content: center;
    /* min-height: 100vh; */
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
