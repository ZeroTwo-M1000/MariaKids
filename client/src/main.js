import { createApp } from "vue"
import { createPinia } from "pinia"

import App from "./App.vue"
import router from "./router"
import "./style.css"
import "boxicons/css/boxicons.min.css"
import axios from "axios"
import { autoAnimatePlugin } from "@formkit/auto-animate/vue"

const app = createApp(App)

export const BASE_URL = "http://localhost:8000"

axios.defaults.baseURL = `${BASE_URL}/api`

app.use(createPinia())
app.use(autoAnimatePlugin)
app.use(router)

app.mount("#app")
