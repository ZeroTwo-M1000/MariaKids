<template>
    <div class="tasks">
        <h1>Контакты</h1>
        <div class="content">
            <iframe
                height="500"
                src="https://yandex.ru/map-widget/v1/?um=constructor%3Aea2eb2878752acf049f3a63dacf28fac522b995768c8598e817657e59079bb0e&amp;source=constructor"
                width="800"
            >
            </iframe>
            <div class="content-info">
                <div>
                    <i class="bx bxs-map-pin" style="color: #ffffff"></i>
                    <p>МДОУ "Детский сад №228"</p>
                </div>
                <div>
                    <i class="bx bx-envelope" style="color: #ffffff"></i>
                    <p>metenova83@bk.ru</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.tasks {
    @apply w-full lg:h-screen flex flex-col items-center justify-center;

    h1 {
        @apply text-5xl mt-20 font-bold text-center;
    }

    .content {
        @apply w-11/12 h-full mx-auto flex flex-col-reverse mt-10 lg:mt-0 lg:flex-row items-center justify-center space-x-10;

        iframe {
            @apply w-11/12 h-[280px] lg:w-[800px] lg:h-[500px] rounded-3xl mt-8 lg:mt-0;
        }

        .content-info {
            @apply flex flex-col space-y-5 items-center lg:items-start;

            div {
                @apply flex items-center space-x-3;

                p {
                    @apply text-xl lg:text-3xl text-white;
                }

                i {
                    @apply text-3xl lg:text-5xl;
                }
            }
        }
    }
}
</style>
