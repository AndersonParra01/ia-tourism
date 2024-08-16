<template>
    <div class="flex items-center justify-between">
        <div>
            <input type="text" placeholder="Search" class="p-2 border rounded" />
        </div>
        <div></div>
        <div class="flex items-end">
            <div v-if="!isUserLoggedIn">
                <button class="bg-blue-500 text-white px-4 py-2 rounded" @click="goToLogin">Login</button>
                <button class="bg-blue-500 text-white px-4 py-2 rounded ml-2" @click="goToRegister">Register</button>
            </div>
            <div v-else class="flex items-center space-x-4">
                <img :src="userImage" alt="Profile" class="rounded-full w-10 h-10" />
                <span class="ml-2">{{ userLogin.username }}</span>
                <button class="bg-blue-500 text-white px-4 py-2 rounded" @click="logout">Salir</button>
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
            return `https://randomuser.me/api/portraits/men/${Math.floor(Math.random() * 100)}.jpg`;
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

        const goToLogin = () => {
            router.push('/login');
        };

        const logout = () => {
            localStorage.removeItem('user');
            isUserLoggedIn.value = false;
            router.push('/login');
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
            userImage
        };
    }
}
</script>