<script setup></script>

<template>
    <div class="home">
        <div class="home-about">
            <div class="home-about-bg">
                <img alt="bg" src="@/assets/bg.jpg" />
            </div>
            <div class="home-about-text">
                <h1>Метенова Мария Николаевна</h1>
                <div class="home-about-text-snap">
                    <span></span>
                    <p>Воспитатель I квалификационной категории МДОУ "Детский сад № 228"</p>
                    <span></span>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.home {
    @apply w-screen h-svh;

    &-about {
        @apply w-screen h-svh flex items-center justify-center;

        &-bg {
            @apply w-full h-full;

            img {
                @apply w-full h-svh object-cover;
                filter: grayscale(100%) opacity(70%);
                animation: filter-grey 1.5s ease forwards;
            }
        }

        &-text {
            @apply w-full lg:w-fit h-svh text-white bg-gray-800/80 backdrop-blur-lg absolute right-0 px-24 flex flex-col justify-center items-center;

            transform: translateX(100%);
            animation: take-left 1s ease forwards;

            h1 {
                @apply text-4xl lg:text-5xl text-center;
            }

            .home-about-text-snap {
                @apply flex items-center space-x-4 mt-2;

                p {
                    @apply text-lg lg:text-xl text-center min-w-80;
                }

                span {
                    @apply w-0 lg:w-10 h-1 lg:h-1 rounded-full bg-white/70;
                }
            }
        }
    }
}

@keyframes take-left {
    0% {
        transform: translateX(100%);
    }
    100% {
        transform: translateX(0);
    }
}

@keyframes filter-grey {
    0% {
        filter: grayscale(100%) opacity(70%);
    }
    100% {
        filter: grayscale(20%) opacity(70%);
    }
}
</style>
