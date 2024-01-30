<template>
    <v-sheet :rounded="'xl'" id="quests">
        <div class="quest" v-for="(value, key) in quests" :key=key>
            No.{{ key }}
            <p>다음 물품을 구해오시오.</p>
            <p v-for="(quest_value, quest_key) in value.quest" :key="quest_key">{{quest_key}}:{{ quest_value }}</p>
            <p>보상</p>
            <p v-for="(reword_value, reword_key) in value.reword.output_items" :key="reword_key">{{reword_key}} 제작 기계</p>
            {{ key }}
            <button @click="quest_clear(key)">완료</button>
        </div>
    </v-sheet>
</template>

<script>
export default {
    name: "QuestsComponent",
    data() {
        return {
            quests: {}
        }
    },
    mounted() {
        this.$axios.get('http://localhost:8000/quests')
            .then(response => {
                this.quests = response.data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },
    methods: {
        quest_clear(id){
            this.$axios.get(`http://localhost:8000/quest_clear/${id}`)
            .then(response => {
                if (response.data.status === "success") {
                    this.quests = response.data.data;
                }
            })
        },
    }
}
</script>

<style>
#quests {
    width: 100%;
    height: 50vh;
    border: 1px solid black;
    padding: 20px;
    overflow: auto;
}
</style>