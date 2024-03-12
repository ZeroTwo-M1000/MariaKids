<template>
    <MainBase
        :data="parent_consultations"
        title="Консультации"
        @create="store.create_parent_consultation($event)"
        @delete="store.delete_parent_consultation($event)"
    ></MainBase>
</template>

<script setup>
import MainBase from "@/components/MainBase.vue"
import { useParentConsultations } from "@/stores/useParentConsultations.js"
import { toRefs } from "vue"

const store = useParentConsultations()

const { parent_consultations } = toRefs(useParentConsultations())
</script>

<style lang="scss" scoped></style>
