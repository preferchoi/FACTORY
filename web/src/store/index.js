import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    factories: {}
  },
  mutations: {
    setFactories(state, factories) {
      state.factories = factories
    },
    appendFactory(state, factory) {
      state.factories = { ...state.factories, [factory.id]: factory }
    },
    updateFactory(state, factory) {
      state.factories[factory.id] = factory
    },
    updateMachine(state, { factoryId, machineId, updatedMachine }) {
      const factory = state.factories[factoryId];
      const machineIndex = factory.machines.findIndex(m => m.id === machineId);
      if (machineIndex !== -1) {
        factory.machines[machineIndex] = updatedMachine;
      }
    }
  },

  actions: {
    getFactories({ commit }) {
      axios.get("http://localhost:8000/get_factories")
        .then(res => {
          commit('setFactories', res.data)
        })
    },
    addFactory({ commit }) {
      axios.get("http://localhost:8000/add_factory")
        .then(res => {
          commit('appendFactory', res.data)
        })
    },
    sizeUp({ commit }, factoryId) {
      axios.get(`http://localhost:8000/size_up_factory/${factoryId}`)
      .then(res => {
        commit('updateFactory', res.data)
      })
    },
    upgradeMachine({ commit, state }, { factoryId, machineId, target }) {
      return axios.get(`http://localhost:8000/upgrade/${machineId}?target=${target}`)
        .then(res => {
          const updatedMachine = { ...state.factories[factoryId].machines.find(m => m.id === machineId) };
          if (target === 'process_time') {
            updatedMachine.process_time = res.data.process_time;
          } else if (target === 'error_rate') {
            updatedMachine.error_rate = res.data.error_rate;
          }
          commit('updateMachine', { factoryId, machineId, updatedMachine });
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
  getters: {

  }
})