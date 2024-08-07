<template>
  <Tourism />
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Tourism from './components/tourism.vue';

@Options({
  components: {
    Tourism,
  },
})
export default class App extends Vue { }
</script>