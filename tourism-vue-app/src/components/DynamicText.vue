<template>
  <div class="dynamic-text">
    <p>{{ displayText }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, onMounted } from 'vue';

export default defineComponent({
  props: {
    text: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const displayText = ref('');
    const index = ref(0);

    const showText = (newText: string) => {
      const words = newText.split(' ');
      const interval = 50; // Tiempo en milisegundos entre cada palabra

      const timer = setInterval(() => {
        if (index.value < words.length) {
          displayText.value += words[index.value] + ' ';;
          index.value++;
        } else {
          clearInterval(timer);
        }
      }, interval);
    };

    onMounted(() => {
      showText(props.text);
    });

    watch(() => props.text, (newText) => {
      // Reiniciar el texto cuando cambie la prop
      displayText.value = '';
      index.value = 0;
      showText(newText);
    });

    return {
      displayText,
    };
  },
});
</script>

<style scoped>
.dynamic-text {
  font-size: 16px;
  font-family: Arial, sans-serif;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>
