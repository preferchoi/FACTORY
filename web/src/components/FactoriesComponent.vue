<template>
  <div>
    <div v-for="(factory_value, factory_key) in factoies" :key=factory_key>
        공장 아이디: {{ factory_value.id }}
        공장 크기: {{ factory_value.size }}
        기계: 
        <div v-for="(machine_value, machine_key) in factory_value.machines" :key="machine_key">
            <MachineComponent :machine=machine_value />
        </div>
    </div>
  </div>
</template>

<script>
import MachineComponent from "./MachineComponent.vue";
export default {
    name: "FactoriesComponent",
    data(){
        return {
            factoies: {}
        }
    },
    components:{
        MachineComponent,
    },
    mounted() {
        this.$axios.get("http://localhost:8000/get_factories")
        .then(res => {
          this.factoies = res.data;
          console.log(res.data);
        })
    }
}
</script>

<style>

</style>