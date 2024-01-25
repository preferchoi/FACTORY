<template>
    <div id="materials">
        <div class="material" v-for="(value, key) in materials" :key=key>
            {{ key }}: {{ value.counter }}
            <button @click="material_cell(key)">판매</button>
            <button @click="material_buy(key)">구매</button>
        </div>
    </div>
</template>

<script>

export default {
    name: "MaterialsComponent",
    data() {
        return {
            materials: {
                "money": { "counter": 0 },
                "iron_ore": { "counter": 0 },
                "coal": { "counter": 0 },
                "sintered_steel": { "counter": 0 },
                "coke": { "counter": 0 },
                "slag": { "counter": 0 },
                "steel": { "counter": 0 },
                "steel_Slab": { "counter": 0 },
                "hot_rolled_plate": { "counter": 0 },
                "cold_rolled_plate": { "counter": 0 },
                "steel_billet": { "counter": 0 },
                "wire_rod": { "counter": 0 },
                "casting": { "counter": 0 },
                "forging": { "counter": 0 },
            },
            sse: null
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
        material_cell(material){
            this.$axios.get(`http://localhost:8000/materials/sell?material=${material}&counter=${1}`)
            .then(response => {
                console.log(response.data);
            })
            console.log(material);
        },
        material_buy(material){
            this.$axios.get(`http://localhost:8000/materials/buy?material=${material}&counter=${1}`)
            .then(response => {
                console.log(response.data);
            })
            console.log(material);
        },
    }
}
</script>

<style>
#materials {
    width: 20%;
    height: 100vh;
    border: 1px solid black;
    padding: 20px;
}</style>