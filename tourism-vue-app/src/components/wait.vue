<template>
    <div
        class="flex flex-col items-center justify-center w-full h-full bg-gradient-to-b from-blue-100 via-white to-green-100">
        <div class="relative">
            <div class="w-32 h-32 rounded-full border-4 border-t-4 border-green-500 animate-spin"></div>
            <div class="absolute inset-0 flex items-center justify-center">
                <img src="./../assets/loading.webp" alt="Turismo" class="w-30 h-30 rounded-full" />

            </div>
        </div>

        <p class="mt-8 text-xl text-gray-700 animate-pulse">Exploring Options...</p>

        <div class="mt-6 flex space-x-4">
            <div class="w-6 h-6 rounded-full bg-blue-400 animate-bounce"></div>
            <div class="w-6 h-6 rounded-full bg-green-400 animate-bounce delay-100"></div>
            <div class="w-6 h-6 rounded-full bg-blue-400 animate-bounce delay-200"></div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Wait',
});
</script>

<style scoped></style>