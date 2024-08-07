<template>
    <div class="container mx-auto p-4">
        <h1 class="text-2xl font-bold mb-4">OpenAI Asistente de Turismo Virtual Ec</h1>
        <input v-model="prompt" type="text" placeholder="Enter a prompt" class="border rounded p-2 mb-4 w-full" />
        <button @click="send" class="bg-blue-500 text-white p-2 rounded">Enviar</button>
        <p class="mt-4">{{ response }}</p>
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

        const send = async () => {
            try {
                isLoading.value = true;
                const data = await getCompletion(prompt.value);
                response.value = data.choices[0].text;
                isLoading.value = false;
            } catch (error) {
                isLoading.value = false;
                console.error('Error fetching completion:', error);
            }
        };

        return { prompt, response, send };
    },
});
</script>