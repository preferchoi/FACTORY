<template>
    <div>
        <p>id: {{ machine.id }}</p>
        <p>process_time: {{ machine.process_time }}</p>
        <p>error_rate: {{ machine.error_rate }}</p>
        <p>input_items: {{ machine.input_items }}</p>
        <p>output_items: {{ machine.output_items }}</p>
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

}
</script>

<style></style>