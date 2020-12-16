<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-3">
                <h4 class="mb-3">Welcome to Youtueb Rater</h4>
                <button v-on:click="getVideos" class="btn btn-success">Get Videos</button>
            </div>
        </div>

        <div class="row mt-3">
           <div class="col-md-6">
              <div class="row mt-5">
                  <div class="col-md-4" v-for="video in videos" v-bind:key="video.id">
                      <p>{{ video.title }}</p>
                      <button class="btn btn-sm btn-primary mb-3" 
                      v-on:click="VideoDetail(video)">Video Detail</button>

                  </div>

              </div>
           </div>

           <div class="col-md-6">
                  <VideoDetail v-bind:videoDetail="videoDetail" />
                  <hr>
           </div>
        </div>

        <div class="row">
          <div class="col-lg-10 offset-1">
            <CreateVideo/>
          </div>
        </div>

    </div>
</template>

<script>
// @ is an alias to /sc
import axios from 'axios'
import VideoDetail from './VideoDetail'
import CreateVideo from './CreateVideo'

export default {
  name: 'home',
  components: {
    VideoDetail,
    CreateVideo
  },
  data () {
    return {
        videos: [],
        videoDetail: Object,
    }
  },
  methods: {
    getVideos() {
        axios.get('http://0.0.0.0:8181/api/videos/')
        .then( res => (this.videos = res.data) )
        .catch(err => console.log(err))
        console.log(this.videos) 
        console.log('test')
    },
    VideoDetail(video) {
      this.videoDetail = video
      console.log(this.videoDetail)
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