<template>
  <div id="body">
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
}
</script>

<style>
#body {
  display: flex;
}
</style>
