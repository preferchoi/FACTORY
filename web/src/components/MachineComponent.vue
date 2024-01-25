<template>
    <div class="machine">
        <p>id: {{ machine.id }}</p>
        <p>process_time: {{ machine.process_time }}</p>
        <p>error_rate: {{ machine.error_rate }}</p>
        <p>input_items: {{ machine.input_items }}</p>
        <p>output_items: {{ machine.output_items }}</p>
        <button @click=run_machine>run</button>
    </div>
</template>

<script>
export default {
    name: "MachineComponent",
    props: {
        machine: {
            type: Object,
            default: () => ({}),
            required: true
        }
    },
    methods: {
        run_machine() {
            this.$axios.get(`http://localhost:8000/run_machine/${this.machine?.id}`)
                .then(res => {
                    console.log(res.data);
                })
        }
    }

}
</script>

<style>
.machine {
    width: 48%;
    margin-bottom: 10px;
    padding: 20px;
    border: 1px solid black;
    box-sizing: border-box;
}
</style>