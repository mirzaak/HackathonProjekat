<template>
  <NavBar/>
  <router-view></router-view>
</template>

<script setup>
import NavBar from './components/NavBar.vue'

</script>

<style>
html, body {
  margin:0;
  padding:0;
  height:100%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  
}
body{

background: rgb(216,181,255);
background: linear-gradient(90deg, rgba(216,181,255,1) 0%, rgba(30,174,152,1) 100%);

}
body::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
body {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>