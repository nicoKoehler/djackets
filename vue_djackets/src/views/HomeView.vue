<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb6">
          Welcome to Djacket
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

      <div class="column is-3" v-for="prod in latestProducts" :key="prod.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="prod.get_thumbnail" alt="">
          </figure>
          <h3 class="is-size-4">{{ prod.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ prod.price }}</p>

          <router-link :to="prod.get_absolute_url" class="button is-dark mt-4">View Details</router-link>

        </div>
      </div>
    </div>


  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios"
export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts: []
    }
  },
  components: {

  },
  mounted(){
    this.getLatestProducts()
    document.title = "Home | Djackets"
  },
  methods:{
    async getLatestProducts(){
      this.$store.commit("setIsLoading", true)
      await axios
        .get("/api/v1/latest-products/")
        .then(res => {
          this.latestProducts = res.data
        })
        .catch(err => {
          console.log(err);
        })

      this.$store.commit("setIsLoading", false)
    }
  }
}
</script>
<style scoped>
.image{
  margin: -1.25rem -1.25rem 0 -1.25rem;
}
</style>