<template>
    <div class="children">
        <h1>Работы детей</h1>
        <p v-if="children_art_works.length === 0">Список пуст</p>
        <div v-auto-animate class="gallery">
            <ChildrenItem v-for="item in children_art_works" :key="item.id" :data="item" />
        </div>
    </div>
</template>

<script setup>
import { useChildrenArtWorks } from "@/stores/useChildrenArtWorks.js"
import { toRefs } from "vue"
import ChildrenItem from "@/components/ChildrenItem.vue"

const { children_art_works } = toRefs(useChildrenArtWorks())
</script>

<style lang="scss" scoped>
.children {
    @apply w-11/12 mx-auto flex flex-col items-center;

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
