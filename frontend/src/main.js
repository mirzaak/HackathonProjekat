import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import AOS from 'aos';
import 'aos/dist/aos.css'; // You can also use <link> for styles
import Swiper from 'swiper';
// import Swiper styles
import 'swiper/css';

AOS.init();
createApp(App).use(router).mount('#app')
