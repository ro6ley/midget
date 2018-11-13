<template>
  <div class="home">
    <img alt="logo" src="../assets/logo.png"><img alt="logo" src="../assets/logo.png">
    <Shorten msg="Welcome to mdgt.url" />

  </div>
</template>

<script>
// @ is an alias to /src
import Shorten from '@/components/Shorten.vue';

export default {
  name: 'home',
  components: {
    Shorten,
  },
};
</script>
