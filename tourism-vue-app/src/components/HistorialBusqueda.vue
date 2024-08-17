<template>
    <div class="flex justify-center mt-2 w-full">
        <!-- Contenedor Principal con una Tarjeta -->
        <div class="bg-white shadow-lg rounded-lg p-6 w-full">
            <!-- Barra de Búsqueda -->
            <div class="flex justify-between items-center mb-4">
                <h1 class="text-2xl font-semibold text-gray-700">Historial de Recomendaciones</h1>
                <div class="relative">
                    <input type="text" v-model="searchQuery" placeholder="Buscar en el historial"
                        class="border rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 w-64" />
                    <i class="bx bx-search absolute left-3 top-2 text-gray-400"></i>
                </div>
            </div>

            <!-- Filtros -->
            <div class="flex mb-6 space-x-4">
                <button @click="sortByDate" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
                    Por fecha
                </button>
                <button @click="groupByCategory"
                    class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-300">
                    Por grupo
                </button>
            </div>

            <!-- Lista de Historial -->
            <div v-for="(group, date) in filteredHistory" :key="date" class="mb-8">
                <h2 class="text-lg font-bold mb-2 text-gray-600">{{ date }}</h2>
                <ul>
                    <li v-for="item in group" :key="item.id"
                        class="py-4 border-b border-gray-200 flex justify-between items-center relative">
                        <div class="flex items-center">
                            <input type="checkbox" class="mr-2" />
                            <span class="text-gray-700">{{ item.time }}</span>
                        </div>
                        <div class="flex items-center">
                            <i class="bx bx-world mr-2 text-green-600"></i>
                            <span class="text-gray-700">{{ item.description }}</span>
                        </div>
                        <div class="text-gray-500">{{ item.url }}</div>

                        <!-- Menú de tres puntos -->
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
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';

export default defineComponent({
    setup() {
        const searchQuery = ref<string>('');
        const history = ref([
            { id: 1, time: '17:10', description: 'Lugar 1', url: 'localhost:3000', date: 'Hoy' },
            { id: 2, time: '16:58', description: 'Lugar 2', url: 'localhost:3000', date: 'Hoy' },
            { id: 3, time: '16:50', description: 'Lugar 3', url: 'localhost:3000', date: 'Ayer' },
            // Más datos de ejemplo aquí...
        ]);

        const menuOpen = ref<number | null>(null); // Controla qué menú desplegable está abierto

        const filteredHistory = computed(() => {
            if (!searchQuery.value) return groupByDate(history.value);
            return groupByDate(
                history.value.filter(item =>
                    item.description.toLowerCase().includes(searchQuery.value.toLowerCase())
                )
            );
        });

        const groupByDate = (items: any[]) => {
            return items.reduce((acc: any, item: any) => {
                if (!acc[item.date]) acc[item.date] = [];
                acc[item.date].push(item);
                return acc;
            }, {});
        };

        const toggleMenu = (id: number) => {
            menuOpen.value = menuOpen.value === id ? null : id; // Alterna el estado del menú
        };

        const deleteItem = (id: number) => {
            history.value = history.value.filter(item => item.id !== id); // Elimina el ítem del historial
            menuOpen.value = null; // Cierra el menú después de eliminar
        };

        return {
            searchQuery,
            filteredHistory,
            toggleMenu,
            deleteItem,
            menuOpen
        };
    }
});
</script>

<style scoped>
.input {
    padding-left: 2.5rem;
    /* Espacio para el ícono de búsqueda */
}
</style>