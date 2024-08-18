<template>
    <div class="fixed top-0 left-0 h-full w-64 bg-blue-800 text-white flex flex-col overflow-y-auto">
        <!-- Logo -->
        <div class="flex items-center justify-center py-6">
            <img src="@/assets/turismo.png" alt="Logo" style="width: 75%; height: 90%;" class="object-contain" />
        </div>

        <router-link to="/tourism">
            <div
                class="font-bold p-4 cursor-pointer hover:bg-blue-700 transition duration-200 ease-in-out flex items-center">
                <i class="bx bx-home mr-2"></i> {{ $t('home') }}
            </div>
        </router-link>
        <router-link to="/historial-busquedas">
            <div
                class="font-bold p-4 cursor-pointer hover:bg-blue-700 transition duration-200 ease-in-out flex items-center">
                <i class="bx bx-history mr-2"></i>{{ $t('searchHistory') }}
            </div>
        </router-link>
        <nav class="flex-1 mt-4">
            <ul>
                <li v-for="place in places" :key="place.id"
                    class="p-4 hover:bg-blue-700 cursor-pointer flex items-center transition-colors duration-200 ease-in-out">
                    <i class="bx bx-map mr-2"></i>
                    {{
                        (place.especific_destination ? place.especific_destination :
                            place.description_place || $t('emptyPlace'))
                            .split(' ')
                            .slice(0, 40)
                            .join(' ')
                        + (place.especific_destination && place.especific_destination.split(' ').length > 40 ? '...' : '')
                    }}
                </li>

            </ul>
        </nav>
    </div>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue';
import { fetchUserPlaces, Place } from '@/services/user';

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
            if (user.id != undefined && user.id != null) {
                getUserPlaces();
            }
        });

        return {
            places,
        };
    },
};
</script>

<style scoped></style>
