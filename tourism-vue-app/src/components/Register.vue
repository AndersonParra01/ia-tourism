<template>
  <div class="flex items-center justify-center m-12 bg-gray-100">
    <form @submit.prevent="handleRegister" class="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
      <div class="flex justify-center mb-6">
        <img src="./../assets/user.png" class="w-24 h-24 rounded-full shadow-md" />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
          <label for="name" class="block text-gray-700 font-bold mb-1">{{ $t('name') }}</label>
          <input v-model="name" type="text" id="name" :placeholder="$t('name')" required
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
        </div>
        <div>
          <label for="lastName" class="block text-gray-700 font-bold mb-1">{{ $t('lastName') }}</label>
          <input v-model="lastName" type="text" id="lastName" :placeholder="$t('lastName')" required
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
        </div>
      </div>
      <div class="mb-4">
        <label for="username" class="block text-gray-700 font-bold mb-1">{{ $t('username') }}</label>
        <input v-model="username" type="text" id="username" :placeholder="$t('enterUsername')" required
          class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label for="password" class="block text-gray-700 font-bold mb-1">{{ $t('password') }}</label>
          <input v-model="password" type="password" id="password" :placeholder="$t('enterPassword')" required
            class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
        </div>
        <div>
          <label for="confirmPassword" class="block text-gray-700 font-bold mb-1">{{ $t('confirmPassword') }}</label>
          <input v-model="confirmPassword" type="password" id="confirmPassword" :placeholder="$t('confirmPassword')"
            required class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" />
        </div>
      </div>
      <button type="submit"
        class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-200">
        {{ $t('register') }}
      </button>
      <p class="text-center mt-4 text-gray-600">
        {{ $t('alreadyHaveAccount') }}
        <router-link to="/login" class="text-blue-500 hover:text-blue-700">{{ $t('login') }}</router-link>
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
        await apiLogin(result.data.username, result.data.password);
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
