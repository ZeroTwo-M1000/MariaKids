import { createRouter, createWebHistory } from "vue-router"
import axios from "axios"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: () => import("../views/HomeView.vue")
        },
        {
            path: "/about",
            name: "about",
            component: () => import("../views/AboutView.vue")
        },
        {
            path: "/tasks",
            name: "tasks",
            component: () => import("../views/LessonNotesView.vue")
        },
        {
            path: "/projects",
            name: "projects",
            component: () => import("../views/ProjectActivitiesView.vue")
        },
        {
            path: "/consultations",
            name: "consultations",
            component: () => import("../views/ParentConsultationsView.vue")
        },
        {
            path: "/children",
            name: "children",
            component: () => import("../views/ChildrenArtworksView.vue")
        },
        {
            path: "/contact",
            name: "contact",
            component: () => import("../views/ContactView.vue")
        },
        {
            path: "/login",
            name: "login",
            component: () => import("../views/LoginView.vue"),
            beforeEnter: async (to, from, next) => {
                try {
                    const response = await axios.get("/auth/isadmin")
                    if (response.data.admin) {
                        next({ name: "home" })
                    } else {
                        next()
                    }
                } catch (e) {
                    next()
                }
            }
        }
    ]
})

export default router
