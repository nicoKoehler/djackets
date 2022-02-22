<template>
<div class="column is-3">
            <div class="box">
            <figure class="image mb-4">
                <img :src="prod.get_thumbnail" alt="">
            </figure>
            <h3 class="is-size-4">{{ prod.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ prod.price }}</p>

            <router-link :to="prod.get_absolute_url" class="button is-dark mt-4">View Details</router-link>

            </div>
        </div>
</template>

<script>
export default {
    name: "ProductBox",
    props: {
        prod: Object
    }
}
</script>

<style scoped>
.image{
  margin: -1.25rem -1.25rem 0 -1.25rem;
}
</style>