<template>
  <div id="body">
    <div style="width: 20%;">
      <MaterialsComponent />
      <QuestsComponent />
    </div>
    <FactoriesComponent />
  </div>
</template>

<script>
import MaterialsComponent from './components/MaterialsComponent.vue';
import QuestsComponent from './components/QuestsComponent.vue';
import FactoriesComponent from "./components/FactoriesComponent.vue";

export default {
  name: 'App',
  components: {
    MaterialsComponent,
    QuestsComponent,
    FactoriesComponent,
  },
}
</script>

<style>
#body {
  display: flex;
}
</style>
