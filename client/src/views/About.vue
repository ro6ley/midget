<template>
  <div class="about">
    <h1>
      About midgt.url
    </h1>

    <p>
      This is a pet project by <a href="http://github.com/ro6ley">ro6ley</a> 
      as an attempt to build a URL shortener using Django + Redis + VueJs.
    </p>

    <AllLinks />
  </div>
</template>

<script>
import AllLinks from '@/components/AllLinks.vue';

export default {
  name: 'about',
  components: {
    AllLinks,
  },
  mounted () {
    this.$store.dispatch('fetchAllLinks');
  },  
};
</script>
