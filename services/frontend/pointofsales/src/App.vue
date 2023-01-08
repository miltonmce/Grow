<script setup>
import NavBar from './components/NavBar.vue'
import HelloWorld from './components/HelloWorld.vue';
</script>

<template>
 <div class="navbar">
  <NavBar/>
 </div>
 <div class="sidebar">

 </div>
 <div class="content">
  <router-view/>
 </div>
</template>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: black;
}

</style>
