<template>
  <div>
    <MaterialsComponent />
    <FactoriesComponent />
  </div>
</template>

<script>
import MaterialsComponent from './components/MaterialsComponent.vue';
import FactoriesComponent from "./components/FactoriesComponent.vue";

export default {
  name: 'App',
  components: {
    MaterialsComponent,
    FactoriesComponent,
  },
  // data() {
  //   return {
  //     data: ''
  //   }
  // },
  // methods: {
  //   getData() {
      
  //   },
  // },
}
</script>

<style></style>
