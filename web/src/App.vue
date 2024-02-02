<template>
  <v-app>
    <v-main class="bg-grey-darken-4">
      <v-row>
        <v-col cols="3">
          <v-container>
            <QuestsComponent/>
            <MaterialsComponent style="margin-top: 10px;"/>

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
}
</script>
