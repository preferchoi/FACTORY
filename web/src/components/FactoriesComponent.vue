<template>
    <v-container id="factories">
        <v-card class="bg-grey-lighten-2" :rounded="'xl'" id="factory" v-for="(factory_value, factory_key) in factories"
            :key=factory_key>
            <template v-slot:title>
                {{ factory_value?.id }}번 공장
            </template>

            <template v-slot:subtitle>
                공장 크기: {{ factory_value?.size }}
                <v-btn v-if="factory_value?.size < 10" x-small density="compact" icon="mdi-plus" @click="size_up(factory_value?.id)"></v-btn>
            </template>
            <template v-slot:text>
                <v-row>
                    <v-col cols="6">
                        <v-row>
                            <v-col
                                v-for="(machine_value, machine_key) in factory_value?.machines.filter((_, index) => index % 2 === 0)"
                                :key="machine_key" cols="12">
                                <MachineComponent :factoryId="factory_key" :machineIndex="machine_key * 2" />
                            </v-col>
                        </v-row>
                    </v-col>

                    <v-col cols="6">
                        <v-row>
                            <v-col
                                v-for="(machine_value, machine_key) in factory_value?.machines.filter((_, index) => index % 2 === 1)"
                                :key="machine_key" cols="12">
                                <MachineComponent :factoryId="factory_key" :machineIndex="machine_key * 2 + 1" />
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
                <v-col col="12" v-if="factory_value?.machines.length < 10 & factory_value?.id != 1">
                    <v-card class="bg-grey-lighten-2" :rounded="'xl'">
                        <v-card-action class="bg-grey-lighten-5 text-center d-flex flex-column align-center justify-center">
                            <v-btn class="bg-grey-darken-2 font-weight-black text-h3" style="height:10vh;width: 100%;"
                                @click="buy_machine">기계 추가 구입</v-btn>
                        </v-card-action>
                    </v-card>
                </v-col>
            </template>
        </v-card>
        <v-card class="bg-grey-lighten-2" :rounded="'xl'" id="factory">
            <v-card-action class="bg-grey-lighten-5 text-center d-flex flex-column align-center justify-center">
                <v-btn class="bg-grey-darken-2 font-weight-black text-h3" style="height:20vh;width: 100%;"
                    @click="buy_factory">공장 추가 구입</v-btn>
            </v-card-action>
        </v-card>
    </v-container>
</template>

<script>
import MachineComponent from "./MachineComponent.vue";
import { mapState, mapActions } from 'vuex'

export default {
    name: "FactoriesComponent",
    computed: {
        ...mapState(['factories'])
    },
    components: {
        MachineComponent,
    },
    methods: {
        ...mapActions(['getFactories', 'addFactory', 'sizeUp']),
        size_up(id) {
            // alert(id)
            this.sizeUp(id)
        },
        buy_factory() {
            this.addFactory()
        },
        buy_machine() {
            alert('개발 진행중')
        }
    },
    mounted() {
        this.getFactories();
    }
}
</script>

<style>
#factories {
    flex-grow: 1;
    padding: 20px;
}

#factory {
    margin-bottom: 20px;
    padding: 20px;
    border: 1px solid black;
}
</style>