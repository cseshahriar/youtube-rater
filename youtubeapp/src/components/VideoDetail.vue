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
    }
  },
  methods: {
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
