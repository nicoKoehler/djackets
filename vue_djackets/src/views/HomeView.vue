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

      <ProductBox
        v-for="prod in latestProducts"
        :key="prod.id"
        :prod="prod"
      />
      
    </div>


  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios"

import ProductBox from "@/components/ProductBox"

export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts: []
    }
  },
  components: {
    ProductBox
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
