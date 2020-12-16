<template>
    <div class="container-fluid">
        <div class="row mt-3">
          <div class="col-md-8 offset-2">
              <p>Title: {{ videoDetail.title }}</p>
              <p>Description: {{ videoDetail.description }}</p>
              <iframe width="350" height="200" :src="videoDetail.url" frameborder="0" 
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                      <br>
                <p>Rating: {{ videoDetail.rating_average }}</p>
          </div>
        </div>

    </div>
</template>

<script>
// @ is an alias to /sc
import axios from 'axios'

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
  }
}
</script>
