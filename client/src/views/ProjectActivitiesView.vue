<template>
    <MainBase :data="project_activities" title="Проекты"></MainBase>
</template>

<script setup>
import MainBase from "@/components/MainBase.vue"
import { useProjectActivities } from "@/stores/useProjectActivities.js"
import { toRefs } from "vue"

const { project_activities } = toRefs(useProjectActivities())
</script>

<style lang="scss" scoped></style>
