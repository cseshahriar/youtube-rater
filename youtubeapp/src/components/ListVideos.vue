<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 offset-3">
                <h4 class="mb-3">Welcome to Youtueb Rater</h4>
                
                <form @submit.prevent="createNewVideo()" class="mb-3">
                  <button class="btn btn-info">Create New</button>
                </form>

                <button v-on:click="getVideos" class="btn btn-success">Get Videos</button>
            </div>
        </div>

        <div class="row mt-3">
           <div class="col-md-6">
              <div class="row mt-5">
                  <div class="col-md-4" v-for="video in videos" v-bind:key="video.id">
                      <p>{{ video.title }}</p>
                      Rating: {{ video.rating_average }}<br>
                      <button class="btn btn-sm btn-primary mb-3" 
                      v-on:click="VideoDetail(video)">Video Detail</button>
                  </div>
              </div>
           </div>

           <div class="col-md-6">
                <!-- listen the event from videoDetail $emmit-->
                <VideoDetail v-bind:videoDetail="videoDetail"
                 v-on:updated="updateVideos()"
                 v-on:deleted="deleteVideo()"
                 />
                <hr>
           </div>
        </div>

        <div class="row">
          <div class="col-lg-10 offset-1">
            <div v-if="createNew">
              <CreateVideo/>
            </div>
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
        createNew:""
    }
  },
  methods: {
    getVideos() {
        axios.get('http://localhost:8181/api/videos/')
        .then( res => (this.videos = res.data) )
        .catch(err => console.log(err))
        console.log(this.videos) 
        console.log('test')
    },
    VideoDetail(video) {
      this.videoDetail = video
      console.log(this.videoDetail)
    },
    createNewVideo() {
      this.createNew = !this.createNew // toggle
    },
    updateVideos(video) {
      this.timer = setTimeout(() => {
          axios.get('http://localhost:8181/api/videos/')
          .then( res => (this.videos = res.data) )
          .catch(err => console.log(err))
          console.log(this.videos) 
          console.log('test')
      }, 600);
    },
    deleteVideo(video) {
      this.timer = setTimeout(() => {
          axios.get('http://localhost:8181/api/videos/')
          .then( res => (this.videos = res.data) )
          .catch(err => console.log(err))
          console.log(this.videos) 
          console.log('test')
      }, 600)
    }
  },
  created () {
    // work a page init
    this.getVideos();
    createNew:false;
  }
}
</script>


<style scoped>
.nicefont {
  font-size: 18px;
  font-family: 'Alatsi', sans-serif;
}
</style>