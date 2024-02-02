<template>
    <v-container id="factories" >
        <v-card class="bg-grey-lighten-2" :rounded="'xl'" id="factory" v-for="(factory_value, factory_key) in factories" :key=factory_key>
            <template v-slot:title>
                {{ factory_value.id }}번 공장
            </template>

            <template v-slot:subtitle>
                공장 크기: {{ factory_value.size }}
            </template>

            <template v-slot:text>
                <v-row>
                    <v-col v-for="(machine_value, machine_key) in factory_value.machines" :key="machine_key" cols="6">
                        <MachineComponent :machine="machine_value" />
                    </v-col>
                </v-row>
            </template>

        </v-card>
    </v-container>
</template>

<script>
import MachineComponent from "./MachineComponent.vue";
export default {
    name: "FactoriesComponent",
    data() {
        return {
            factories: {}
        }
    },
    components: {
        MachineComponent,
    },
    mounted() {
        this.$axios.get("http://localhost:8000/get_factories")
            .then(res => {
                this.factories = res.data;
                console.log(res.data);
            })
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