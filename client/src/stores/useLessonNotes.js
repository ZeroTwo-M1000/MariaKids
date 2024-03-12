import { defineStore } from "pinia"
import { computed, ref } from "vue"
import axios from "axios"

export const useLessonNotes = defineStore("lesson_notes", () => {
    const lesson_notes = computed(() => {
        const lesson_notes = ref([])
        axios.get("/lesson-notes/").then((response) => {
            lesson_notes.value = response.data
        })
        return lesson_notes
    })

    return {
        lesson_notes
    }
})
