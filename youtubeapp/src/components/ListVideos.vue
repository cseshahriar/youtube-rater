<template>
    <div class="">
        <div class="row">
            <div class="col-md-5 text-center">
                <h4>Welcome to Youtueb Rater</h4>
                <button v-on:click="getVideos" class="btn btn-success">Get Videos</button>
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
        videos: []
    }
  },
  methods: {
    getVideos() {
        axios.get('http://0.0.0.0:8181/api/videos/')
        .then( res => (this.videos == res.data) )
        .catch(err => console.log(err))
        console.log(this.videos)
    }
  }
}
</script>
