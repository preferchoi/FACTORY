<template>
    <v-sheet :rounded="'xl'" id="quests">
        <v-card class="quest" v-for="(value, key) in quests" :key=key>
            <v-card-title>
                No.{{ key }}
            </v-card-title>
            <v-card-text>
                <p>다음 물품을 구해오시오.</p>
                <v-chip v-for="(quest_value, quest_key) in value.quest" :key="quest_key">
                    <img :src="getImagePath(quest_key)" :alt="item" style="width:20%;height:auto%;"/> 
                    :{{ quest_value }}
                </v-chip>
                <p>보상</p>
                <v-chip v-for="(reword_value, reword_key) in value.reword.output_items" :key="reword_key">
                    <img :src="getImagePath(reword_key)" :alt="item" style="width:20%;height:auto%;"/> - 제작 기계
                </v-chip>
            </v-card-text>
            <v-card-actions class="d-flex justify-end">
                <v-btn class="bg-grey-darken-3" @click="quest_clear(key)">완료</v-btn>
            </v-card-actions>
        </v-card>
    </v-sheet>
</template>
<!-- api 수정해서 단일 객체만 보내기로 했으니 사이즈 조절. 퀘스트가 없을 경우 없다고 표시하기. -->

<script>
export default {
    name: "QuestsComponent",
    data() {
        return {
            quests: {}
        }
    },
    mounted() {
        this.$axios.get('http://localhost:8000/quest')
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
        getImagePath(item) {
            return require(`@/assets/${item}.png`);
        }
    }
}
</script>

<style>
#quests {
    width: 100%;
    height: auto;
    padding: 20px;
    overflow: auto;
}
#quests::-webkit-scrollbar {
  display: none;
}
</style>