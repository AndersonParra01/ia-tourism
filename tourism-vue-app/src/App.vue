<template>
  <div class="flex min-h-screen bg-gray-100">
    <Sidebar />
    <div class="flex-1 p-6">
      <div class="flex-1 p-6 ml-64">
        <Header />
        <router-view />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Sidebar from './components/layout/Sidebar.vue';
import Header from './components/layout/Header.vue';

@Options({
  components: {
    Sidebar,
    Header,
  },
})
export default class App extends Vue { }
</script>

<style scoped></style>
