import { defineStore } from "pinia"
import { computed, ref } from "vue"
import axios from "axios"

export const useChildrenArtWorks = defineStore("children_art_works", () => {
    const children_art_works = computed(() => {
        const children_art_works = ref([])
        axios.get("/children-artworks/").then((response) => {
            children_art_works.value = response.data
        })
        return children_art_works
    })

    const create_children_art_work = (fd) => {
        axios.post("/children-artworks/", fd).then(() => {
            window.location.reload()
        })
    }
    const delete_children_art_work = (id) => {
        axios.delete(`/children-artworks/${id}`).then(() => {
            window.location.reload()
        })
    }

    return {
        children_art_works,
        create_children_art_work,
        delete_children_art_work
    }
})
