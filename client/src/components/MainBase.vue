<template>
    <div class="base">
        <h1>{{ title }}</h1>
        <div v-if="$admin" class="create">
            <textarea placeholder="Заголовок" type="text" @change="fd.append('title', $event.target.value)"></textarea>
            <input type="file" @change="fd.append('file', $event.target.files[0])" />
            <button @click="$emit('create', fd)">Добавить</button>
        </div>
        <div v-auto-animate class="list">
            <p v-if="data.length === 0">Список пуст</p>
            <BaseItem v-for="item in data" v-else :key="item.id" :data="item" @delete="$emit('delete', item.id)" />
        </div>
    </div>
</template>

<script setup>
import BaseItem from "@/components/Base/BaseItem.vue"
import FormData from "form-data"

const fd = new FormData()

defineProps({
    title: {
        type: String,
        required: true
    },
    data: {
        type: Array,
        required: true
    }
})
</script>

<style lang="scss" scoped>
.base {
    h1 {
        @apply text-5xl mt-20 font-bold text-center;
    }

    .create {
        @apply flex flex-col items-center justify-center mt-10 space-y-5;

        input {
            @apply w-1/2;
        }

        button {
            @apply w-8/12 lg:w-1/4 h-12 text-white rounded-2xl bg-gray-700 hover:bg-gray-600 transition-all duration-200;
        }

        textarea {
            @apply w-11/12 lg:w-1/2 h-24 bg-gray-700 rounded-lg px-3 py-2 outline-none;
        }
    }

    .list {
        @apply flex flex-col items-center justify-center mt-10 space-y-5;

        p {
            @apply text-2xl;
        }
    }
}
</style>
