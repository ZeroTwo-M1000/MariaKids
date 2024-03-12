<template>
    <div class="login">
        <h1>Вход</h1>
        <div class="form">
            <input v-model="login" placeholder="Логин" type="text" />
            <input v-model="password" placeholder="Пароль" type="password" />
            <button @click="loginFunc">Войти</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue"
import axios from "axios"
import router from "@/router/index.js"

const login = ref("")
const password = ref("")

function loginFunc() {
    if (login.value === "" || password.value === "") return
    axios
        .post("/auth/login", { username: login.value, password: password.value })
        .then((response) => {
            localStorage.setItem("token", response.data)
            router.push({ name: "home" })
        })
        .catch(() => {
            login.value = ""
            password.value = ""
        })
}
</script>

<style lang="scss" scoped>
.login {
    h1 {
        @apply text-5xl mt-20 font-bold text-center;
    }

    .form {
        @apply w-11/12 lg:w-1/2 mx-auto flex flex-col items-center justify-center space-y-5 mt-10;

        input {
            @apply w-11/12 h-8 text-neutral-950 lg:h-10 lg:w-1/2 px-3 rounded-lg outline-none;
        }

        button {
            @apply w-11/12 lg:w-1/2 h-12 text-white rounded-2xl bg-gray-700 hover:bg-gray-600 transition-all duration-200;
        }
    }
}
</style>
