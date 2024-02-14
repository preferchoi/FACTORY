<template>
    <v-list-item class="d-flex align-center" @click="isOpen = !isOpen">
        <v-row>
            <v-col col="3">
                <v-list-item-avatar>
                    <img :src="getImagePath(name)" :alt="name" width="50px"/>
                </v-list-item-avatar>
            </v-col>
            <v-col col="9">
                <v-list-item-content>
                    <v-list-item-title>{{ name }}: {{ material.counter }}</v-list-item-title>
                </v-list-item-content>
            </v-col>
            <v-col col="12">
                <v-list-item-action v-if="isOpen">
                    <v-btn color="grey darken-3" @click.stop="material_cell(name)" class="ma-2">판매</v-btn>
                    <v-btn color="grey darken-3" @click.stop="material_buy(name)" class="ma-2">구매</v-btn>
                </v-list-item-action>
            </v-col>
        </v-row>
    </v-list-item>
</template>

<script>

export default {
    name: "M_cellComponent",
    data() {
        return {
            isOpen: false
        }
    },
    props: {
        name: {
            type: String,
            default: 'money',
            require: true
        },
        material: {
            type: Object,
            default: () => ({}),
            required: true
        },
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

<style></style>