<template>
    <v-card class="bg-grey-lighten-2" :rounded="'xl'" id="materials">
        <v-list :rounded="'xl'" v-for="(value, key) in materials" :key="key" style="margin-bottom: 10px;">
            <M_cellComponent :name="key" :material="value" />
        </v-list>
    </v-card>
</template>

<script>
import M_cellComponent from './M_cellComponent.vue';
export default {
    name: "MaterialsComponent",
    components: {
        M_cellComponent,
    },
    data() {
        return {
            materials: {
                "money": { "counter": 0 },
                "iron_ore": { "counter": 0 },
                "coal": { "counter": 0 },
                "sintered_steel": { "counter": 0 },
                "cokes": { "counter": 0 },
                "slag": { "counter": 0 },
                "steel": { "counter": 0 },
                "steel_slab": { "counter": 0 },
                "hot_rolled_plate": { "counter": 0 },
                "cold_rolled_plate": { "counter": 0 },
                "steel_billet": { "counter": 0 },
                "wire_rod": { "counter": 0 },
                "casting": { "counter": 0 },
                "forging": { "counter": 0 },
            },
            sse: null,
        }
    },
    mounted() {
        this.sse = new EventSource('http://localhost:8000/materials_sse'); // 서버 URL로 SSE 연결
        this.sse.onmessage = (event) => {
            this.materials = JSON.parse(event.data); // 서버로부터 오는 데이터를 처리
        };
        this.sse.onerror = (error) => {
            console.error('SSE Error:', error);
            this.sse.close(); // 에러 발생 시 SSE 연결 종료
        };

        this.$axios.get('http://localhost:8000/materials')
            .then(response => {
                this.materials = response.data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },
    beforeUnmount() {
        if (this.sse) {
            this.sse.close(); // 컴포넌트 제거 전 SSE 연결 종료
        }
    },
    methods: {
        material_cell(material) {
            this.$axios.get(`http://localhost:8000/materials/sell?material=${material}&counter=${1}`)
                .then(response => {
                    console.log(response.data);
                })
            console.log(material);
        },
        material_buy(material) {
            this.$axios.get(`http://localhost:8000/materials/buy?material=${material}&counter=${1}`)
                .then(response => {
                    console.log(response.data);
                })
            console.log(material);
        },
        getImagePath(item) {
            return require(`@/assets/${item}.png`);
        }
    }
}
</script>

<style>
#materials {
    width: 100%;
    /* height: 50vh; */
    border: 1px solid black;
    padding: 20px;
}
</style>