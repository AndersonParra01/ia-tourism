<template>
    <div class="fixed top-0 left-0 h-full w-64 bg-gray-900 text-white flex flex-col overflow-y-auto">
        <router-link to="/tourism">
            <div class="text-xl font-bold p-4 cursor-pointer hover:bg-gray-200 transition duration-200 ease-in-out hover:p-4">Home</div>
        </router-link>
        <router-link to="/recomendaciones">
            <div class="text-xl font-bold p-4 cursor-pointer hover:bg-gray-200 transition duration-200 ease-in-out hover:p-4">Recomendaciones</div>
        </router-link>
        <div class="text-xl font-bold p-4">Historial de Busquedas</div>
        <nav class="flex-1">
            <ul>
                <li v-for="place in places" :key="place.id"
                    class="p-4 hover:bg-gray-800 cursor-pointer flex items-center">
                    {{ place.name }}
                </li>
            </ul>
        </nav>
    </div>
</template>


<script lang="ts">
import { ref, onMounted } from 'vue';
import { fetchUserPlaces, Place } from '@/services/user'; // Importa el servicio

export default {
    name: 'Sidebar',
    setup() {
        const userId = ref('');
        const places = ref<Place[]>([]);

        const getUserPlaces = async () => {
            try {
                console.log('Fetching places for user ID:', userId.value);
                const response = await fetchUserPlaces(userId.value);
                console.log('Response Data:', response);
                places.value = response.places;
            } catch (error) {
                console.error('Error fetching user places:', error);
            }
        };

        onMounted(() => {
            const user = JSON.parse(localStorage.getItem('user') || '{}');
            console.log('USER SIDE', user);
            userId.value = user.id;
            console.log('ID', userId);
            getUserPlaces();
        });

        return {
            places,
        };
    },
};
</script>