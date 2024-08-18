<template>
    <div class="flex justify-center mt-2 w-full">
        <div class="bg-white shadow-lg rounded-lg p-6 w-full">
            <div v-if="isLoading" class="text-center text-blue-500">
                <i class="fas fa-spinner fa-spin mr-2"></i> Cargando...
            </div>

            <div v-else>
                <div class="flex justify-between items-center mb-4">
                    <h1 class="text-2xl font-semibold text-gray-700">Historial de Recomendaciones</h1>

                    <div class="flex items-center space-x-4">
                        <div v-if="selectedItems.length != 0">
                            <button @click="deleteSelectedItems"
                                class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600">
                                Eliminar Seleccionados
                            </button>
                        </div>

                        <div class="relative">
                            <input type="text" v-model="searchQuery" placeholder="Buscar en el historial"
                                class="border rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 w-64" />
                            <i
                                class="bx bx-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                        </div>
                    </div>
                </div>

                <div v-for="(group, date) in filteredHistory" :key="date" class="mb-8">
                    <span class="block text-2xl">
                        {{ new Date(date).toLocaleDateString('es-ES', {
                            day: '2-digit', month: 'long', year: 'numeric'
                        }) }}
                        a las
                        {{ new Date(date).toLocaleTimeString('es-ES', {
                            hour: '2-digit', minute: '2-digit', second:
                                '2-digit'
                        }) }}
                    </span>
                    <ul>
                        <li v-for="item in group" :key="item.id"
                            class="py-4 border-b border-gray-200 flex justify-between items-center relative">
                            <div class="flex items-center">
                                <input type="checkbox" v-model="selectedItems" :value="item.id" class="mr-2" />
                                <span class="text-gray-700">{{ item.time }}</span>
                            </div>
                            <div class="flex items-center">
                                <i class="bx bx-world mr-2 text-green-600"></i>
                                <span class="text-gray-700">{{ item.description_place }}</span>
                            </div>
                            <div class="text-gray-500">{{ item.url }}</div>

                            <div class="relative">
                                <i @click="toggleMenu(item.id)"
                                    class="bx bx-dots-vertical-rounded text-gray-400 cursor-pointer"></i>
                                <div v-if="menuOpen === item.id"
                                    class="absolute right-0 bg-white shadow-md rounded-md mt-2 p-2 z-50">
                                    <button @click="deleteItem(item.id)"
                                        class="block w-full text-left text-red-500 hover:bg-gray-100 px-4 py-2">
                                        Eliminar
                                    </button>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import { Place, fetchUserPlaceDelete, fetchUserPlaces } from '@/services/user';

export default defineComponent({
    setup() {
        const searchQuery = ref<string>('');
        const history = ref<Place[]>([]);
        const menuOpen = ref<number | null>(null);
        const selectedItems = ref<number[]>([]);
        const isLoading = ref<boolean>(true); // Variable de estado para la carga

        const loadPlaces = async () => {
            try {
                const userSave = JSON.parse(localStorage.getItem('user') || '{}');
                const user = await fetchUserPlaces(userSave.id);
                history.value = user.places;
            } catch (error) {
                console.error('Error al obtener los lugares:', error);
            } finally {
                isLoading.value = false; // Finaliza la carga
            }
        };

        const filteredHistory = computed(() => {
            if (!searchQuery.value) return groupByDate(history.value);
            return groupByDate(
                history.value.filter(item =>
                    item.description_place && item.description_place.toLowerCase().includes(searchQuery.value.toLowerCase())
                )
            );
        });

        const groupByDate = (items: Place[]) => {
            return items.reduce((acc: any, item: Place) => {
                if (!acc[item.created_at]) acc[item.created_at] = [];
                acc[item.created_at].push(item);
                return acc;
            }, {});
        };

        const toggleMenu = (id: number) => {
            menuOpen.value = menuOpen.value === id ? null : id;
        };

        const deleteItem = async (id: number) => {
            try {
                const userSave = JSON.parse(localStorage.getItem('user') || '{}');
                await fetchUserPlaceDelete(userSave.id, id);
                history.value = history.value.filter(item => item.id !== id);
                menuOpen.value = null;
                loadPlaces();
            } catch (error) {
                console.error('Error al eliminar el lugar:', error);
            }
        };

        const deleteSelectedItems = async () => {
            try {
                const userSave = JSON.parse(localStorage.getItem('user') || '{}');
                for (const id of selectedItems.value) {
                    await fetchUserPlaceDelete(userSave.id, id);
                }
                loadPlaces();
                window.location.reload();
                selectedItems.value = [];
            } catch (error) {
                console.error('Error al eliminar los lugares:', error);
            }
        };

        onMounted(() => {
            loadPlaces();
        });

        return {
            searchQuery,
            filteredHistory,
            toggleMenu,
            deleteItem,
            menuOpen,
            selectedItems,
            deleteSelectedItems,
            isLoading // Devuelve el estado de carga
        };
    }
});
</script>

<style scoped>
.input {
    padding-left: 2.5rem;
}

h2 {
    font-size: 1.2rem;
    color: #1E3A8A;
}
</style>
