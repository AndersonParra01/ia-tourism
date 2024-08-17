<template>
  <div class="flex items-center justify-center m-14 bg-gray-100">
    <form @submit.prevent="handleLogin" class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full">
      <div class="flex justify-center mb-6">
        <img src="./../assets/user.png" class="w-24 h-24 rounded-full shadow-md" />
      </div>
      <div class="mb-4 text-left">
        <label for="user" class="block text-gray-700 font-bold mb-1">Usuario:</label>
        <input type="text" id="user" v-model="userName" placeholder="Ingresa tu usuario" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <div class="mb-6 text-left">
        <label for="password" class="block text-gray-700 font-bold mb-1">Contraseña:</label>
        <input type="password" id="password" v-model="password" placeholder="Ingresa tu contraseña" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <button type="submit"
        class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-200">
        Login
      </button>
      <p class="text-center mt-4 text-gray-600">
        ¿No tienes cuenta?
        <router-link to="/register" class="text-blue-500 hover:text-blue-700">Regístrate aquí</router-link>
      </p>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { apiLogin } from "@/services/auth";

export default defineComponent({
  setup() {
    const userName = ref("");
    const password = ref("");
    const router = useRouter();

    const handleLogin = async () => {
      try {
        const result = await apiLogin(userName.value, password.value);
        if (!result.success) {
          throw new Error("Error al iniciar sesión");
        }
        localStorage.setItem("user", JSON.stringify(result.user));
        window.location.href = '/tourism';
      } catch (error) {
        alert("Error al iniciar sesión");
      }
    };

    return {
      userName,
      password,
      handleLogin,
    };
  },
});
</script>

<style scoped></style>
