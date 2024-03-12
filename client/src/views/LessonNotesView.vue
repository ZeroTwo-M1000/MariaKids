<template>
    <MainBase :data="lesson_notes" title="Задания"></MainBase>
</template>

<script setup>
import MainBase from "@/components/MainBase.vue"
import { useLessonNotes } from "@/stores/useLessonNotes.js"
import { toRefs } from "vue"

const { lesson_notes } = toRefs(useLessonNotes())
</script>

<style lang="scss" scoped></style>
