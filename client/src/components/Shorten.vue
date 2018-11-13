<template>
  <div>
    <div class="hello">
      <h1>{{ msg }}</h1>
      <p>
        We'll shorten your long urls for you. Simply, fast and reliably. Try it out 👇🏽
      </p>

    </div>
    <!-- Div to display the shortened URL -->
    <div class="shortUrlDiv">
      <a v-bind:href=" this.$store.state.apiUrl + urlId " target="_blank"> {{ shortUrl }} </a>
    </div>

    <!-- Div to display any errors -->
    <div class="errorMsgDiv">
      {{ errorMsg }}
    </div>

    <!-- Div to display the form -->
    <div class="inputForm">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show" >

        <b-input-group prepend="Long URL">

        <b-form-input id="longUrlInput" type="text" v-model="form.longUrl" required>
          </b-form-input>
        <b-input-group-append>
            <b-btn type="submit" variant="outline-success">Shorten</b-btn>
            <b-btn type="reset" variant="outline-danger">Cancel</b-btn>
          </b-input-group-append>
        </b-input-group>

      </b-form>
    </div>

  </div>
</template>

<script>
// import axios
import axios from 'axios';

export default {
  data () {
    return {
      form: {
        longUrl: '',
      },
      shortUrl: '',
      errorMsg: '',
      urlId: '',
      show: true
    }
  },
  name: 'Shorten',
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.errorMsg = '';
      this.shortUrl = '';
      axios
        .post(this.$store.state.apiUrl + 'api/links/', {"url": this.form.longUrl})
        .then(response => { 
          this.shortUrl = 'mdgt.url/' + response.data.url;
          this.urlId = response.data.url;
           })
        .catch(err => { 
          this.errorMsg = err.response.data.msg;
          });
    },
    onReset(evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.longUrl = '';
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.errorMsg = '';
      this.shortUrl = '';
      this.$nextTick(() => { this.show = true; });
    },
  },
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.inputForm {
  width: 40%;
  text-align: center;
  margin: 0 auto;
}

.shortUrlDiv {
}

.errorMsgDiv {
  margin: 0.5rem;
  color: red;
}
</style>
