<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Youtube Rater</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#">Registration</a>
        </li>
      </ul>

      <form class="d-flex" @submit.prevent="login" v-if="token==null">
        <input class="form-control me-2" v-model="username" id="username" name="username" type="text" placeholder="Username">
        <input class="form-control me-2" v-model="password" id="password" name="password" type="password" placeholder="Password">
        <button class="btn btn-outline-success" type="submit">Login</button>
      </form>

      <form @submit.prevent="logout" v-if="token!=null">
        <button class="btn btn-danger" type="submit">Logout</button>
      </form>

    </div>
  </div>
</nav>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Header',
    components: {

    },
    data() {
      return {
        username: '',
        password: '',
        token:localStorage.getItem('user-token') || null,
      }
    },
    methods: {
        login() {
            axios.post('http://localhost:8181/api/auth/', {
              username: this.username,
              password: this.password,
            })
            .then( res =>  {
                this.token = res.data.token
                console.log(this.token)
                localStorage.setItem('user-token', res.data.token)
              }
            )
            .catch( err => {
              localStorage.removeItem('user-token')
            })
        },
        logout() {
          localStorage.removeItem('user-token')
          this.token = null
        }
    }
}
</script>