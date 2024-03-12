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

    return {
        children_art_works
    }
})
