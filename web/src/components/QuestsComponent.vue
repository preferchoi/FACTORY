<template>
    <div>
        <v-card class="quest" v-for="(value, key) in quests" :key=key :rounded="'xl'">
            <div v-if="key!=0">
                <v-card-title>
                    No.{{ key }}
                </v-card-title>
                <v-card-text>
                    <text>다음 물품을 구해오시오.</text>
                    <v-chip v-for="(quest_value, quest_key) in value.quest" :key="quest_key" style="margin-bottom: 5px;">
                        <img :src="getImagePath(quest_key)" :alt="item" style="width:15%;height:auto%;" />
                        :{{ quest_value }}
                    </v-chip>
                    <text>보상</text>
                    <v-chip v-for="(reword_value, reword_key) in value.reword.output_items" :key="reword_key"
                        style="margin-bottom: 10px;">
                        <img :src="getImagePath(reword_key)" :alt="item" style="width:15%;height:auto%;" /> - 제작 기계
                    </v-chip>
                    <v-card-actions class="d-flex justify-end">
                        <v-btn class="bg-grey-darken-3" @click="quest_clear(key)">완료</v-btn>
                    </v-card-actions>
                </v-card-text>
            </div>
            <div v-if="key==0">
                <v-card-title>
                    모든 퀘스트 완료
                </v-card-title>
                <v-card-text>
                    <text>가장 효율적인 공장을 구현해보세요.</text>
                </v-card-text>
            </div>
        </v-card>
    </div>
</template>
<!-- api 수정해서 단일 객체만 보내기로 했으니 사이즈 조절. 퀘스트가 없을 경우 없다고 표시하기. -->

<script>
import { mapActions } from 'vuex'
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
        ...mapActions(['getFactoies']),
        quest_clear(id) {
            this.$axios.get(`http://localhost:8000/quest_clear/${id}`)
                .then(response => {
                    if (response.data.status === "success") {
                        this.quests = response.data.data;
                        this.getFactoies();
                    }
                })
        },
        getImagePath(item) {
            return require(`@/assets/${item}.png`);
        },
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