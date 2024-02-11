<template>
    <v-card>
        <v-card-title>{{ machine.id }}번 기계</v-card-title>
        <v-card-subtitle>소모 시간 - {{ machine.process_time }}s / 불량률 - {{ machine.error_rate * 100 }}%</v-card-subtitle>
        <v-card-text>
            <v-divider :thickness="1" style="margin-bottom: 10px;"></v-divider>
            <text class="d-flex justify-center">투입</text>
            <v-row>
                <v-col cols="4" v-for="(quantity, item) in machine.input_items" :key="item">
                    <img :src="getImagePath(item)" :alt="item" style="width: 100%;height: auto;" /> 
                    <text class="d-flex justify-center">{{ item }}: {{ quantity }}</text>
                </v-col>
            </v-row>
            <v-divider :thickness="1" style="margin-top: 10px; margin-bottom: 10px;"></v-divider>
            <text class="d-flex justify-center">반환</text>
            <v-row>
                <v-col cols="4" v-for="(quantity, item) in machine.output_items" :key="item">
                    <img :src="getImagePath(item)" :alt="item" style="width: 100%;height: auto;" /> 
                    <text class="d-flex justify-center">{{ item }}: {{ quantity }}</text>
                </v-col>
            </v-row>
            
            <v-divider :thickness="1" style="margin-top: 10px;"></v-divider>
            
            <v-card-actions class="d-flex justify-end">
                <v-btn v-if="loading" class="bg-grey-darken-3">
                    loading
                </v-btn>
                <v-btn v-if="!loading" class="bg-grey-darken-3" @click=run_machine>
                    run
                </v-btn>
            </v-card-actions>
        </v-card-text>
        
    </v-card>
</template>

<script>
export default {
    name: "MachineComponent",
    data() {
        return {
            loading: false,
        }
    },
    props: {
        machine: {
            type: Object,
            default: () => ({}),
            required: true
        }
    },
    methods: {
        run_machine() {
            this.loading = true
            this.$axios.get(`http://localhost:8000/run_machine/${this.machine?.id}`)
                .then(res => {
                    console.log(res.data);
                    this.loading = false
                })
                .catch(err => {
                    this.loading = false
                    console.log(err);
                })
        },

        getImagePath(item) {
            return require(`@/assets/${item}.png`);
        }

    }

}
</script>

<style></style>