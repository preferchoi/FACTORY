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
    upgradeMachine({ commit, state }, { factoryId, machineId, target }) {
      return axios.get(`http://localhost:8000/upgrade/${machineId}?target=${target}`)
        .then(res => {
          const updatedMachine = { ...state.factories[factoryId].machines.find(m => m.id === machineId) };
          if (target === 'process_time') {
            updatedMachine.process_time = res.data.process_time;
          } else if (target === 'error_rate') { 
            updatedMachine.error_rate = res.data.error_rate;
          }

          // 'updateMachine' 뮤테이션을 커밋하여 스토어의 상태를 업데이트합니다.
          commit('updateMachine', { factoryId, machineId, updatedMachine });
        })
        .catch(error => {
          console.error('Error upgrading machine:', error);
        });
    },
  },
  getters: {

  }
})