<template>
    <MainBase
        :data="project_activities"
        title="Проекты"
        @create="store.create_project_activity($event)"
        @delete="store.delete_project_activity($event)"
    ></MainBase>
</template>

<script setup>
import MainBase from "@/components/MainBase.vue"
import { useProjectActivities } from "@/stores/useProjectActivities.js"
import { toRefs } from "vue"

const store = useProjectActivities()

const { project_activities } = toRefs(useProjectActivities())
</script>

<style lang="scss" scoped></style>
