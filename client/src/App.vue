<template>
    <AppNavigation />
    <div class="app">
        <router-view />
    </div>
</template>

<script setup>
import AppNavigation from "@/components/Navigation/AppNavigation.vue"
</script>

<style lang="scss">
.app {
    @apply overflow-x-hidden;
}
</style>
