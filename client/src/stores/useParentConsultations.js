import { defineStore } from "pinia"
import { computed, ref } from "vue"
import axios from "axios"

export const useParentConsultations = defineStore("parent_consultations", () => {
    const parent_consultations = computed(() => {
        const parent_consultations = ref([])
        axios.get("/parent-consultations/").then((response) => {
            parent_consultations.value = response.data
        })
        return parent_consultations
    })

    const create_parent_consultation = (fd) => {
        axios
            .post("/parent-consultations/", fd, {
                params: {
                    title: fd.get("title")
                }
            })
            .then(() => {
                window.location.reload()
            })
    }

    const delete_parent_consultation = (id) => {
        axios.delete(`/parent-consultations/${id}`).then(() => {
            window.location.reload()
        })
    }

    return {
        parent_consultations,
        create_parent_consultation,
        delete_parent_consultation
    }
})
