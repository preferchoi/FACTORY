<template>
    <div>
        <div v-for="(value, key) in materials" :key=key>
            {{ key }}: {{ value.counter }}
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
    },
    beforeUnmount() {
        if (this.sse) {
            this.sse.close(); // 컴포넌트 제거 전 SSE 연결 종료
        }
    }
}
</script>

<style></style>