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

    const create_project_activity = (fd) => {
        axios
            .post("/project-activities/", fd, {
                params: {
                    title: fd.get("title")
                }
            })
            .then(() => {
                window.location.reload()
            })
    }

    const delete_project_activity = (id) => {
        axios.delete(`/project-activities/${id}`).then(() => {
            window.location.reload()
        })
    }

    return {
        project_activities,
        create_project_activity,
        delete_project_activity
    }
})
