<template>
    <div class="children">
        <h1>Работы детей</h1>
        <div v-if="true" class="create">
            <input type="file" @change="fd.append('file', $event.target.files[0])" />

            <button @click="store.create_children_art_work(fd)">Добавить</button>
        </div>
        <p v-if="children_art_works.length === 0">Список пуст</p>
        <div v-auto-animate class="gallery">
            <ChildrenItem v-for="item in children_art_works" :key="item.id" :data="item" @delete="store.delete_children_art_work(item.id)" />
        </div>
    </div>
</template>

<script setup>
import { useChildrenArtWorks } from "@/stores/useChildrenArtWorks.js"
import { toRefs } from "vue"
import ChildrenItem from "@/components/ChildrenItem.vue"

const fd = new FormData()

const store = useChildrenArtWorks()

const { children_art_works } = toRefs(useChildrenArtWorks())
</script>

<style lang="scss" scoped>
.children {
    .create {
        @apply flex flex-col items-center justify-center mt-10 space-y-5;

        input {
            @apply w-8/12 lg:w-1/4 h-12 text-white;
        }

        button {
            @apply w-8/12 lg:w-1/4 h-12 text-white rounded-2xl bg-gray-700 hover:bg-gray-600 transition-all duration-200;
        }
    }

    h1 {
        @apply text-5xl mt-20 font-bold text-center;
    }

    p {
        @apply text-2xl mt-10 text-center;
    }

    .gallery {
        @apply w-full flex flex-col lg:flex-row lg:flex-wrap mt-10;
    }
}
</style>
