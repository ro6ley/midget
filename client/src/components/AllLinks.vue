<template>
  <div>
    <hr> 
    <h2> Shortened Links </h2>
    <div class="responseMsgDiv">
      {{ responseMsg }}
    </div>

    <div class="errorMsgDiv">
      {{ errorMsg }}
    </div>

    <div class="allLinksDiv">
      <b-list-group v-for="(value, key, index) in allLinks" :key="index">
        <b-list-group-item> 
          <span class="listItem">
          <a v-bind:href=" apiUrl + key " target="_blank">mdgt.url/{{ key }}</a> 👉🏽 {{ value }} 
          </span>
          <b-button class="deleteBtn" variant="outline-danger" size="sm" v-on:click="deleteLink(key)">❌</b-button> 
        </b-list-group-item>
      </b-list-group>
      
    </div>
  </div>

</template>

<script>
// import axios
import axios from 'axios';
import { mapState, mapActions } from 'vuex';

export default {
  computed: mapState([
    'allLinks',
    'count',
    'responseMsg',
    'errorMsg',
    'apiUrl',
  ]),
  data () {
    return {
    }
  },
  name: 'AllLinks',
  methods: {
    getAllLinks(){
      this.$store.dispatch('fetchAllLinks');

    },
    deleteLink(linkId) {
      axios
        .delete(this.$store.state.apiUrl + linkId)
        .then(response => {
          delete this.allLinks[linkId];
          this.$store.dispatch('deleteLink', linkId);
          this.$store.dispatch('setResponseMsg', "Link deleted successfully.");
          this.$forceUpdate();
        })
        .catch(err => {
          console.err(err);
          this.$store.dispatch('setErrorMsg', err.response.data.msg);
        });
    },
    ...mapActions({
      // deleteLink: 'deleteLink',
    })
  },
}
</script>

<style>
.allLinksDiv {
  width: 40%;
  text-align: center;
  margin: 0 auto;
}

.errorMsgDiv {
  margin: 0.5rem;
  color: red;
}

.deleteBtn {
  float: right;
}

.listItem {
  float: left;
}

</style>
