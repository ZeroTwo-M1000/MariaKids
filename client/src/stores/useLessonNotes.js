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

    const create_lesson_note = (fd) => {
        axios
            .post("/lesson-notes/", fd, {
                params: {
                    title: fd.get("title")
                }
            })
            .then(() => {
                window.location.reload()
            })
    }

    const delete_lesson_note = (id) => {
        axios.delete(`/lesson-notes/${id}`).then(() => {
            window.location.reload()
        })
    }

    return {
        lesson_notes,
        create_lesson_note,
        delete_lesson_note
    }
})
