import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import axios from 'axios';

loadFonts()

const app = createApp(App)
app.config.globalProperties.$axios = axios;
app.use(vuetify).mount('#app')
