<template>
    <div class="flex min-h-screen bg-gray-100">
        <Sidebar />
        <div class="flex-1 p-6">
            <Header />
            <!-- Aquí renderizamos el componente según la ruta -->
            <router-view />
        </div>
    </div>
</template>

<script lang="ts">
import Sidebar from './components/Sidebar.vue'
import Header from './components/Header.vue'

export default {
    components: {
        Sidebar,
        Header,
    },
}
</script>

<style scoped></style>