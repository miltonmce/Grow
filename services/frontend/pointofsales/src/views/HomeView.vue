<template>
  <div class="main-content">
  <aside style="background-color:aqua ;">
    gsdg
  </aside>
  <main style="background-color: brown;">
    fdgdf
  </main>
</div>
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>

<style>
.main-content{
  display: flex;
}
</style>
