import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import store from './store'
import axios from 'axios';

loadFonts()

const app = createApp(App)
app.config.globalProperties.$axios = axios;
app.use(vuetify).use(store).mount('#app')
