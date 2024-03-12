<script setup>
import { BASE_URL } from "@/main.js"
import { ref } from "vue"

defineProps({
    data: {
        type: Object,
        required: true
    }
})

const download = (data) => {
    window.open(BASE_URL + data.link)
}

const img = ref()

const toggleImg = () => {
    img.value.classList.toggle("container")
}
</script>

<template>
    <div class="children">
        <div class="children-img">
            <img ref="img" :src="BASE_URL + data.link" alt="img" @click="toggleImg" />
            <button class="dow" @click="download(data)">Скачать</button>
            <button class="del" @click="$emit('delete', data.id)">Удалить</button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.children {
    @apply basis-1/3 p-3;

    .children-img {
        @apply w-full h-full rounded-xl overflow-hidden relative;

        img {
            @apply w-full max-h-[400px] h-full object-cover rounded-xl cursor-pointer;
        }

        .dow {
            @apply absolute bottom-0 left-0 right-0 w-full hover:scale-110 transition-all duration-300 p-3 bg-gray-800/40 backdrop-blur-lg text-white text-center font-bold rounded-b-xl;
        }

        .del {
            @apply absolute top-0 left-0 right-0 w-full hover:scale-110 transition-all duration-300 p-3 bg-red-500/40 backdrop-blur-lg text-white text-center font-bold rounded-t-xl;
        }
    }
}

.container {
    object-fit: contain !important;
}
</style>
