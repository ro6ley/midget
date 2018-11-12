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
import { mapState } from 'vuex';

export default {
  computed: mapState([
    'allLinks',
    'count',
    'responseMsg',
    'errorMsg'
  ]),
  data () {
    return {
      // allLinks: this.$store.state.allLinks,
      // count: this.$store.state.count,
      // errorMsg: this.$store.state.errorMsg,
      // responseMsg: this.$store.state.responseMsg,
      apiUrl: this.$store.state.apiUrl
    }
  },
  name: 'AllLinks',
  methods: {
    getAllLinks(){
      this.errorMsg = '';
      this.responseMsg = '';
      this.$store.dispatch('fetchAllLinks');
      // this.$forceUpdate();
      // axios
      //   .get(this.$store.state.apiUrl + 'all')
      //   .then(response => {
      //     this.allLinks = response.data.links;
      //     this.count = response.data.count;
      //     this.responseMsg = response.data.msg;
      //   })
      //   .catch(err => {
      //     this.errorMsg = err.response.data.msg;
      //   });
    },
    deleteLink(linkId) {
      this.errorMsg = '';
      this.responseMsg = '';
      this.$store.dispatch('deleteLink', linkId);
      // axios
      //   .delete(this.$store.state.apiUrl + linkId)
      //   .then(response => {
      //     delete this.allLinks[linkId];
      //     this.responseMsg = response.data.msg;
      //   })
      //   .catch(err => {
      //     this.errorMsg = err.response.data.msg;
      //   });
    },
  },
  mounted () {
    this.$store.dispatch('fetchAllLinks');
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
