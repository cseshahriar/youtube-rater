<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-5 text-center">
                <h4>Welcome to Youtueb Rater</h4>
                <button v-on:click="getVideos" class="btn btn-success">Get Videos</button>
            </div>

            <div class="col-md-7">
              <div class="row">
                  <div class="col-md-4" v-for="video in videos" v-bind:key="video.id">
                      <p>{{ video.title }}</p>
                      <iframe width="250" height="250" :src="video.url" frameborder="0" 
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                      
                      <p>{{ video.description }}</p>
                      Rating: {{ video.rating_average }} <br>
                      <button class="btn btn-sm btn-primary mt-2 mb-3">Details</button>
                  </div>
              </div>

              <p v-for="video in videos" v-bind:key="video.id" class="nicefont">
              </p>
            </div>
        </div>

    </div>
</template>

<script>
// @ is an alias to /sc
import axios from 'axios'

export default {
  name: 'home',
  components: {
    
  },
  data () {
    return {
        videos: [],
    }
  },
  methods: {
    getVideos() {
        axios.get('http://0.0.0.0:8181/api/videos/')
        .then( res => (this.videos = res.data) )
        .catch(err => console.log(err))
        console.log(this.videos) 
        console.log('test')
    }
  },
  created () {
    this.getVideos()
  }
}
</script>


<style scoped>
.nicefont {
  font-size: 18px;
  font-family: 'Alatsi', sans-serif;
}
</style>