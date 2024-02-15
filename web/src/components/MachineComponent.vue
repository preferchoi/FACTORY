<template>
    <v-card>
        <v-card-title class="d-flex justify-space-between">
            <span>{{ machine.id }}번 기계</span>
            <v-icon v-if="isOpen" @click="isOpen = !isOpen">mdi-close</v-icon>
            <v-icon v-if="!isOpen" @click="isOpen = !isOpen">mdi-chevron-down</v-icon>
        </v-card-title>
        <v-card-subtitle>
            <span>
                소모 시간 - {{ machine.process_time }}s
            </span>
            <v-btn x-small density="compact" icon="mdi-plus" @click="upgrade_machine('process_time')"></v-btn>
            <span>
                / 불량률 - {{ machine.error_rate * 100 }}%
            </span>
            <v-btn density="compact" icon="mdi-plus" @click="upgrade_machine('error_rate')"></v-btn>
        </v-card-subtitle>
        <v-expand-transition v-show="isOpen">
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
                    <v-btn :loading="loading" class="bg-grey-darken-3" @click=run_machine>
                        run
                    </v-btn>
                </v-card-actions>
            </v-card-text>
        </v-expand-transition>
    </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "MachineComponent",
    data() {
        return {
            isOpen: false,
            loading: false,
        }
    },
    props: {
        factoryId: String,
        machineIndex: Number
    },
    computed: {
        ...mapState(['factories']),
        machine() {
            const factory = this.factories[this.factoryId];
            return factory ? factory.machines[this.machineIndex] : null;
        }
    },
    methods: {
        ...mapActions([]),
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
        upgrade_machine(target) {
            this.$store.dispatch('upgradeMachine', { factoryId: this.factoryId, machineId: this.machine.id, target });
        },

        getImagePath(item) {
            return require(`@/assets/${item}.png`);
        }

    }

}
</script>

<style></style>