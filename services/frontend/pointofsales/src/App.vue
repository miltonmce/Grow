<script setup>
import NavBar from "./components/navbar/NavBar.vue"
import SideBar from "./components/sidebar/SideBar.vue"
</script>

<template>
  <div id="wrapper">
    <header>
      <NavBar />
    </header>
    <aside>
      <SideBar />
    </aside>
    <main>
      <router-view></router-view>
    </main>
  </div>
  

</template>

<style scoped>
#wrapper>header {
  grid-area: navbar;
  background-color: #8ca0ff;
}

#wrapper>aside {
  grid-area: sidebar;
  background-color: #ffa08c;
}

#wrapper>main {
  grid-area: content;
  background-color: #ffff64;
}

@media screen and (max-width: 480px) {
  
}

@media screen and (max-width:768px) {

  
}
@media screen and (max-width:1024px) {
    #wrapper {
        display: grid;
        width: 100%;
        height: 100vh;
        grid-template-areas:
          "sidebar navbar"
          "sidebar content";
        grid-template-rows: 50px 1fr 30px;
        grid-template-columns: 150px 1fr;
      }
}
@media (min-width: 1025px){
  #wrapper {
      display: grid;
      width: 100%;
      height: 100vh;
      grid-template-areas:
        "sidebar navbar"
        "sidebar content";
      grid-template-rows: 50px 1fr 30px;
      grid-template-columns: 150px 1fr;
    }
}
</style>
