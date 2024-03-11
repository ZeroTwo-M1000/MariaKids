<script setup>
import { ref } from "vue"

const navigation = ref()

function toggleNavigation() {
    navigation.value.classList.toggle("hidden")
}

function closeNavigation() {
    navigation.value.classList.add("hidden")
}

const routes = ref([
    { to: "home", name: "Главная" },
    { to: "about", name: "Обо мне" },
    { to: "tasks", name: "Конспекты заданий" },
    { to: "projects", name: "Проектная деятельность" },
    { to: "consultations", name: "Консультации для родителей" },
    { to: "children", name: "Работы детей" },
    { to: "contact", name: "Контакты" }
])
</script>

<template>
    <nav class="navigation">
        <button class="navigation-burger" @click="toggleNavigation">
            <i class="bx bx-menu"></i>
        </button>
        <div ref="navigation" class="navigation-menu hidden">
            <div class="navigation-menu-items">
                <router-link v-for="route in routes" :key="route.to" :to="{ name: route.to }" class="navigation-menu-link" @click="closeNavigation">
                    {{ route.name }}
                </router-link>
            </div>
        </div>
    </nav>
</template>

<style lang="scss" scoped>
.navigation {
    @apply bg-gray-600/50 backdrop-blur-3xl w-full fixed top-0 z-50 py-2 lg:py-4 flex flex-col items-center justify-center;

    &-burger {
        @apply lg:hidden;

        i {
            @apply text-3xl m-0 p-0 text-white hover:text-white cursor-pointer transition-all duration-300;
        }
    }

    &-menu {
        @apply items-center lg:flex;

        .router-link-active {
            @apply bg-gray-800 rounded-md;
            @apply lg:bg-transparent;
            color: white !important;
        }

        &-items {
            @apply flex flex-col items-center justify-center mt-2 lg:mt-0 space-y-3 lg:space-x-5 lg:space-y-0 lg:flex-row;

            .navigation-menu-link {
                @apply font-normal lg:text-white/50 px-3 py-1 lg:px-0 lg:py-0 hover:text-white transition-all duration-200;
            }
        }
    }
}
</style>
