import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    factories: {}
  },
  mutations: {
    setFactoies(state, factories) {
      state.factories = factories
    }
  },
  actions: {
    getFactoies({ commit }) {
      axios.get("http://localhost:8000/get_factories")
      .then(res => {
        commit('setFactoies', res.data)
      })
    }
  },
  getters: {

  }
})