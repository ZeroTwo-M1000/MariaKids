<template>
    <div class="base">
        <h1>{{ title }}</h1>
        <div v-auto-animate class="list">
            <p v-if="data.length === 0">Список пуст</p>
            <BaseItem v-for="item in data" v-else :key="item.id" :data="item" />
        </div>
    </div>
</template>

<script setup>
import BaseItem from "@/components/Base/BaseItem.vue"

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

    .list {
        @apply flex flex-col items-center justify-center mt-10 space-y-5;

        p {
            @apply text-2xl;
        }
    }
}
</style>
