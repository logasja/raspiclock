<template>
    <div>
        <swatches v-model="color" />
    </div>
</template>

<script>
    import Swatches from 'vue-swatches'

    import "vue-swatches/dist/vue-swatches.min.css"

    export default {
        name: 'ColorChanger',
        components: {Swatches},
        data () {
            return {
                color: '#1CA085'
            }
        }
    }
</script>

<style scoped>

</style>