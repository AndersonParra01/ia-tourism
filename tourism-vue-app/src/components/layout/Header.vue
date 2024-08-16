<template>
    <div class="flex items-center justify-between bg-white p-4 shadow-md">
        <div class="relative">
            <div v-if="isUserLoggedIn">
                <input type="text" placeholder="Search"
                    class="p-2 pl-10 border rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500" />
                <svg class="w-5 h-5 text-gray-400 absolute top-1/2 left-3 transform -translate-y-1/2" fill="none"
                    stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M21 21l-4.35-4.35M17 10a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>

                <button
                    class="ml-2 bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition duration-300"
                    @click="goToHome">
                    Inicio
                </button>

            </div>
            <div v-else>
                <button class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition duration-300"
                    @click="goToHome">
                    Inicio
                </button>
            </div>
        </div>

        <div class="flex items-center space-x-6">
            <div v-if="!isUserLoggedIn">
                <button class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition duration-300"
                    @click="goToLogin">
                    Iniciar Sesión
                </button>
                <button
                    class="bg-blue-500 text-white px-4 py-2 rounded-full ml-2 hover:bg-blue-600 transition duration-300"
                    @click="goToRegister">
                    Registro
                </button>
            </div>
            <div v-else class="flex items-center space-x-4">
                <img :src="userImage" alt="Profile" class="rounded-full w-10 h-10 border-2 border-gray-200" />
                <span class="font-semibold text-gray-800">{{ userLogin.username }}</span>
                <button class="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600 transition duration-300"
                    @click="logout">
                    Salir
                </button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'Header',
    setup() {
        const router = useRouter();
        const isUserLoggedIn = ref(false);
        const userLogin = ref({
            username: '',
            names: '',
            lastnames: ''
        });

        const userImage = ref('');

        const getRandomImage = () => {
            return `https://randomuser.me/api/portraits/men/${Math.floor(
                Math.random() * 100
            )}.jpg`;
        };
        const checkUser = () => {
            const user = localStorage.getItem('user');
            if (user) {
                isUserLoggedIn.value = true;
                const parsedUser = JSON.parse(user);
                console.log(parsedUser);
                userLogin.value = parsedUser;
            } else {
                isUserLoggedIn.value = false;
            }
        };
        const goToRegister = () => {
            router.push('/register');
        };

        const goToHome = () => {
            router.push('/tourism');
        };

        const goToLogin = () => {
            router.push('/login');
        };

        const logout = () => {
            localStorage.removeItem('user');
            isUserLoggedIn.value = false;
            window.location.href = '/login';

        };

        onMounted(() => {
            checkUser();
            userImage.value = getRandomImage();
        });

        return {
            goToRegister,
            goToLogin,
            checkUser,
            logout,
            isUserLoggedIn,
            userLogin,
            userImage,
            goToHome
        };
    }
};
</script>

<style scoped></style>