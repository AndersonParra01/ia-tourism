<template>
    <div class="m-4 mx-auto p-3">
        <h1 class="text-2xl font-bold mb-4">OpenAI Asistente de Turismo Virtual Ec</h1>
        <div>
            <label for="language">Seleccione su idioma:</label>
            <select v-model="language" id="language">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
            </select>
        </div>
        <input v-model="prompt" type="text" placeholder="Enter a prompt" class="border rounded p-2 mb-4 w-full" />
        <button @click="send" class="bg-blue-500 text-white p-2 rounded">Enviar</button>
        <p class="mt-4">{{ response }}</p>

        <h3></h3>

    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { getCompletion } from './../services/ia';

export default defineComponent({
    setup() {
        const prompt = ref('');
        const response = ref('');
        const isLoading = ref(false);
        let language: 'en' | 'es' | 'fr' = 'en';


        const send = async () => {
            try {
                isLoading.value = true;
                const result = await getCompletion(prompt.value);
                console.log(result);
                response.value = result.response;
                isLoading.value = false;
            } catch (error) {
                isLoading.value = false;
                console.error('Error fetching completion:', error);
            }
        };

        return { prompt, response, send, language };
    },
});
</script>