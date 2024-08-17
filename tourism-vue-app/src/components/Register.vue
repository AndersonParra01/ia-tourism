<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <form @submit.prevent="handleRegister" class="bg-white p-8 rounded-lg shadow-lg max-w-sm w-full">
      <div class="flex justify-center mb-6">
        <img src="./../assets/user.png" class="w-24 h-24 rounded-full shadow-md" />
      </div>
      <div class="mb-4 text-left">
        <label for="name" class="block text-gray-700 font-bold mb-1">Nombre</label>
        <input v-model="name" type="text" id="name" placeholder="Ingresa tu nombre" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <div class="mb-4 text-left">
        <label for="lastName" class="block text-gray-700 font-bold mb-1">Apellido</label>
        <input v-model="lastName" type="text" id="lastName" placeholder="Ingresa tu apellido" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <div class="mb-4 text-left">
        <label for="username" class="block text-gray-700 font-bold mb-1">Nombre de usuario</label>
        <input v-model="username" type="text" id="username" placeholder="Crea un nombre de usuario" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <div class="mb-4 text-left">
        <label for="password" class="block text-gray-700 font-bold mb-1">Contraseña</label>
        <input v-model="password" type="password" id="password" placeholder="Crea una contraseña segura" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <div class="mb-6 text-left">
        <label for="confirmPassword" class="block text-gray-700 font-bold mb-1">Confirmar contraseña</label>
        <input v-model="confirmPassword" type="password" id="confirmPassword" placeholder="Repite tu contraseña"
          required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <button type="submit"
        class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-200">
        Registrarse
      </button>
      <p class="text-center mt-4 text-gray-600">
        ¿Ya tienes una cuenta?
        <router-link to="/login" class="text-blue-500 hover:text-blue-700">Inicia sesión aquí</router-link>
      </p>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { apiLogin, apiRegister } from "@/services/auth";

export default defineComponent({
  setup() {
    const name = ref("");
    const lastName = ref("");
    const username = ref("");
    const password = ref("");
    const confirmPassword = ref("");
    const router = useRouter();

    const handleRegister = async () => {
      if (password.value !== confirmPassword.value) {
        alert('Las contraseñas no coinciden');
        return;
      }

      try {
        const user = {
          names: name.value,
          lastnames: lastName.value,
          username: username.value,
          password: password.value,
        };
        const result = await apiRegister(user);
        console.log("XD", result);
        console.log(result.data.username, user.password);
        await apiLogin(result.data.username, result.data.password)
        localStorage.setItem('user', JSON.stringify(result.data));
        window.location.href = '/tourism';
      } catch (error) {
        console.log(error);
        alert('Error al registrar usuario');
      }
    };

    return {
      name,
      lastName,
      username,
      password,
      confirmPassword,
      handleRegister,
    };
  },
});
</script>

<style scoped></style>
