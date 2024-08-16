<template>
    <div class="fixed top-0 left-0 h-full w-64 bg-gray-900 text-white flex flex-col overflow-y-auto">
        <div class="text-xl font-bold p-4">Historial de Busquedas</div>
        <nav class="flex-1">
            <ul>
                <li class="p-4 hover:bg-gray-800 cursor-pointer flex items-center">
                    <i class="icon-class mr-2"></i>Tables
                </li>
                <li class="p-4 hover:bg-gray-800 cursor-pointer flex items-center">
                    <i class="icon-class mr-2"></i>Forms
                </li>
                <li class="p-4 hover:bg-gray-800 cursor-pointer flex items-center">
                    <i class="icon-class mr-2"></i>UI
                </li>
                <li class="p-4 hover:bg-gray-800 cursor-pointer flex items-center">
                    <i class="icon-class mr-2"></i>Responsive
                </li>
                <!-- Agrega más elementos según sea necesario -->
            </ul>
        </nav>
        <div class="p-4 bg-blue-600 hover:bg-blue-500 cursor-pointer">
            Logout
        </div>
    </div>
</template>

<script lang="ts">
export default {
    name: 'Sidebar',
}
</script>