<template>
    <div class="container-fluid">
        <div class="row mt-3">
          <div class="col-md-8 offset-2">
              <a :href="videoDetail.url" target="_blank">
                  <h2>{{ videoDetail.title }}</h2>
              </a>
              <p>Description: {{ videoDetail.description }}</p>
              <iframe width="350" height="200" :src="videoDetail.url" frameborder="0" 
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <br>
                <p>Category: {{ videoDetail.category }} , Subcategory: {{ videoDetail.subcategory }}, Rating: {{ videoDetail.rating_average }}</p>
                <p>Comments: {{ videoDetail.comment_list }}</p>
                <!-- $emit() create event, for component communication -->
                <form id="formvideo" @submit.prevent="giveRating"
                @submit="$emit('updated', videoDetail)"
                >
                  <div class="form-group">
                    <label for="">Give a Rating</label>
                    <input type="text" name="stars" id="stars" v-model="stars" class="form-control">
                  </div>
                  
                  <div class="form-group">
                    <label for="">Comments</label>
                    <textarea type="text" name="comments" id="comments" v-model="comments" rows="3" class="form-control"></textarea>
                  </div>

                  <button class="btn btn-sm btn-success" type="submit">Submit Rating</button>
                </form>
                <button class="btn btn-danger mt-2 mb-3" v-on:click="videoDelete(videoDetail)">Delete</button>
          </div>
        </div>

    </div>
</template>

<script>
// @ is an alias to /sc
import axios from 'axios'
import { TokenService } from '../storage/service'

export default {
  name: 'VideoDetail',
  components: {
  },
  props: {
      videoDetail: {}
  },
  data () {
    return {
      stars: '',
      comments: ''
    }
  },
  methods: {
    giveRating(stars, comments) {
      this.token = TokenService.getToken()
      var postData = {
        stars : this.stars,
        comments: this.comments
      };
      
      let axiosConfig = {
        headers: {
          'Authorization': 'Token '+ this.token 
        }
      };

      axios.post(`http://localhost:8181/api/videos/${this.videoDetail.id}/rate_video/`, 
        postData, axiosConfig
      )
      .then(res => console.log(res.data))
      .catch( err => console.log(err))
    },
    videoDelete(videoDetail) {
      console.log(videoDetail.id, 'on delete id')
      console.log(this.token, 'on delete')
      var postData = {
        video: this.videoDetail.id,
      };

      let axiosConfig = {
        headers: {
          'Authorization': 'Token '+ this.token 
        }
      };

      axios.delete(`http://localhost:8181/api/videos/${this.videoDetail.id}`, 
        axiosConfig
      )
      .then( res => console.log(res.data))
      .catch(err => console.log(err))
    }
  }, 
  created() {
    let token
    this.token = TokenService.getToken()
    console.log(this.token, ' created method')
  }
}
</script>
