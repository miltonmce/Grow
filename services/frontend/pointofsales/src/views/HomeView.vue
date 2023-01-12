<template>
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Assumenda facilis dolore doloribus neque blanditiis exercitationem, delectus rem, cumque atque perspiciatis ab praesentium. Soluta amet modi officia nesciunt expedita voluptatem debitis.
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>

<style>
.main-content {
  display: flex;
}
</style>
