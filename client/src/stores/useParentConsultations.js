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

    return {
        parent_consultations
    }
})
