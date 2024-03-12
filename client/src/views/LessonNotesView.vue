<template>
    <MainBase :data="lesson_notes" title="Задания" @create="store.create_lesson_note($event)" @delete="store.delete_lesson_note($event)"></MainBase>
</template>

<script setup>
import MainBase from "@/components/MainBase.vue"
import { useLessonNotes } from "@/stores/useLessonNotes.js"
import { toRefs } from "vue"

const store = useLessonNotes()

const { lesson_notes } = toRefs(useLessonNotes())
</script>

<style lang="scss" scoped></style>
