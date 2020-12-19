<template>
    <div class="">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card w-100">
                    <div class="card-body">
                        <h4 class="card-title">Register</h4>
                        
                        <form id="formvideo" @submit.prevent="createUser">
                            <div class="row">
                                <div class="col">
                                    <label for="username">Username</label>
                                    <input type="text" class="form-control" v-model="username" name="username" id="username">
                                </div>
                            </div>

                            <div class="row">
                                <div class="col">
                                    <label for="password">Password</label>
                                    <input type="text" class="form-control" v-model="password" name="password" id="password">
                                </div>
                            </div>

                            <button type="submit" class="btn btn-primary mt-3">Register</button>
                        </form>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'register',
    components: {
    },
    data() {
        return {
            username:null,
            password:null
        }
    },
    methods: {
        createUser() {
            axios.post('http://localhost:8181/api/users/', {
                username: this.username,
                password: this.password
            })
            .then(res => console.log(res))
            .catch(err => console.log(err))
            this.$router.push('/')
        }
    }
}
</script>