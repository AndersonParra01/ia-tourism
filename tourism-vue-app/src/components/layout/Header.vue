<template>
    <div class="flex items-center justify-between">
        <div>
            <input type="text" placeholder="Search (ctrl+k)" class="p-2 border rounded" />
        </div>
        <div class="flex items-center">
            <span class="mr-4">Sample menu</span>
            <img src="https://via.placeholder.com/40" alt="Profile" class="rounded-full w-10 h-10" />
            <span class="ml-2">John Doe</span>
        </div>
    </div>
</template>

<script lang="ts">
export default {
    name: 'Header',
}
</script>