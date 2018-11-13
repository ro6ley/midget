import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiUrl: 'http://127.0.0.1:8000/',
    allLinks: [],
    linksCount: 0,
    responseMsg: '',
    errorMsg: '',
  },
  getters: {

  },
  setters: {

  },
  mutations: {
    setLinks(state, results) {
      state.allLinks = results.links;
      state.linksCount = results.count;
    },
    deleteLink(state, linkId) {
      delete state.allLinks[linkId];
      state.linksCount -= 1;
    },
    setResponseMsg(state, msg) {
      state.responseMsg = msg;
    },
    setErrorMsg(state, msg) {
      state.errorMsg = msg;
    },
  },
  actions: {
    fetchAllLinks({ commit }) {
      axios
        .get(this.state.apiUrl + 'all')
        .then((response) => {
          commit('setLinks', response.data);
          commit('setResponseMsg', response.data.msg);
        })
        .catch((err) => {
          commit('setErrorMsg', err.response.data.msg);
        });
    },
    deleteLink({ commit }, linkId) {
      commit('deleteLink', linkId);
    },
    setResponseMsg({ commit }, msg) {
      commit('setResponseMsg', msg);
    },
  },
});
