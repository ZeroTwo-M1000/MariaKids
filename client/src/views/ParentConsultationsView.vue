<template>
    <MainBase :data="parent_consultations" title="Консультации"></MainBase>
</template>

<script setup>
import MainBase from "@/components/MainBase.vue"
import { useParentConsultations } from "@/stores/useParentConsultations.js"
import { toRefs } from "vue"

const { parent_consultations } = toRefs(useParentConsultations())
</script>

<style lang="scss" scoped></style>
