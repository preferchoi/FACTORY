<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col cols="3">
          <v-container>
            <MaterialsComponent />
            <v-divider :thickness="8" style="margin-top: 10px; margin-bottom: 10px;"></v-divider>
            <QuestsComponent />
          </v-container>
        </v-col>

        <v-col cols="9">
          <v-container>
            <FactoriesComponent />
          </v-container>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import FactoriesComponent from './components/FactoriesComponent.vue';
import MaterialsComponent from './components/MaterialsComponent.vue';
import QuestsComponent from './components/QuestsComponent.vue';

export default {
  name: 'App',

  components: {
    FactoriesComponent,
    MaterialsComponent,
    QuestsComponent,
  },

  data: () => ({
    //
  }),
}
</script>
