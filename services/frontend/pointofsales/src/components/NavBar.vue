
<script>
export default {
  name: "NavBar",
};
</script>

<template>
  <nav>
  <div class="forall">
    <router-link class="nav-link" to="/">Home</router-link>
  </div>
  <div  class="logged">
    <router-link  class="nav-link" to="/dashboard">Dashboard</router-link>
    <router-link  class="nav-link" to="/profile">Profile</router-link>
  </div>
  <div class="logout nav-left">
    <router-link  class="nav-link" to="/register">Register</router-link>
    <router-link  class="nav-link" to="/login">LogIn</router-link>
  </div>
</nav>
</template>


<style>
  nav{
    display: flex;
    width: 100vh;
  }
  .nav-link{
    text-decoration: none;
    color: black;
    padding: 15px;
  }
  .nav-left{
    
  }
</style>