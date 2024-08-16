<template>
    <div>
        <h2 class="text-2xl font-bold mb-6">Overview</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <StatCard title="Clients" value="512" icon="👥" growth="+12%" growthClass="text-green-500" />
            <StatCard title="Sales" value="$7,770" icon="🛒" growth="-12%" growthClass="text-red-500" />
            <StatCard title="Performance" value="256%" icon="📈" growth="Overflow" growthClass="text-yellow-500" />
        </div>
    </div>
</template>

<script lang="ts">
import StatCard from './StatCard.vue'

export default {
    components: {
        StatCard,
    },
}
</script>