import { defineStore } from "pinia"
import { computed, ref } from "vue"
import axios from "axios"

export const useProjectActivities = defineStore("project_activities", () => {
    const project_activities = computed(() => {
        const project_activities = ref([])
        axios.get("/project-activities/").then((response) => {
            project_activities.value = response.data
        })
        return project_activities
    })

    return {
        project_activities
    }
})
