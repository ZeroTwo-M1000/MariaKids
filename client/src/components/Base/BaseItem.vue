<script setup>
import { BASE_URL } from "@/main.js"

defineProps({
    data: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <div class="item">
        <div class="item-text">
            <h1>{{ data.title }}</h1>
            <p>{{ data.date.substring(0, 10).split("-").reverse().join(".") }}</p>
        </div>
        <a :href="BASE_URL + data.link" download>
            <p>Скачать</p>
            <i class="bx bx-cloud-download" style="color: #ffffff"></i>
        </a>
    </div>
</template>

<style lang="scss" scoped>
.item {
    @apply w-11/12 lg:w-1/2 h-full space-x-7 flex justify-between items-center py-5 px-8 lg:px-10 bg-gray-700 backdrop-blur-lg rounded-2xl;

    .item-text {
        h1 {
            @apply text-xl lg:text-3xl;
        }

        p {
            @apply text-sm lg:text-xl mt-5 text-white/50;
        }
    }

    a {
        @apply text-lg lg:text-xl flex items-center justify-center text-center lg:space-x-3 bg-gray-600 py-2 px-3 lg:py-2 lg:px-5 rounded-xl;

        p {
            @apply hidden lg:block;
        }

        i {
            @apply text-2xl lg:text-3xl;
        }
    }
}
</style>
