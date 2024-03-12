<script setup></script>

<template>
    <div class="about">
        <div class="about-img">
            <img alt="foto" src="@/assets/foto.jpg" />
        </div>
        <div class="about-text">
            <h1>Метенова Мария Николаевна</h1>
            <div class="about-text-p">
                <p>Дата рождения: 09.03.1983</p>
                <p>Образование: высшее, Ярославский государственный педагогический университет им. Ушинского в 2005г.</p>
                <p>Специальность: Учитель биологи и химии</p>
                <p>Место работы: МДОУ "Детский сад №228"</p>
                <p>Должность: Воспитатель</p>
                <p>Общий педагогический стаж: 8 лет</p>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.about {
    @apply w-full lg:h-screen flex flex-col lg:flex-row-reverse lg:space-x-3;
    @apply pt-12 lg:pt-5;

    &-img {
        @apply w-full h-full basis-1/2 flex items-center justify-center;
        animation: take-left 1s ease forwards;

        img {
            @apply w-fit h-full lg:w-4/6 lg:h-4/5 object-cover lg:rounded-3xl;
        }
    }

    &-text {
        @apply w-full h-full basis-1/2 flex flex-col items-center lg:items-end justify-center px-5 lg:px-0 lg:pl-16;
        animation: take-right 1s ease forwards;

        h1 {
            @apply mt-10 lg:mt-0 text-3xl lg:text-5xl font-bold text-center lg:text-end;
        }

        &-p {
            @apply flex flex-col items-center lg:items-end justify-center mb-12 lg:mb-0;

            p {
                @apply w-full lg:w-fit text-lg lg:text-xl text-start py-3 px-8 bg-gray-700/40 rounded-3xl mt-4;
            }
        }
    }
}

@keyframes take-right {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(0);
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
</style>
