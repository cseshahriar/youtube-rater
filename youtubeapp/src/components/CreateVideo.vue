<template>
    <div class="">
        <div class="row">
            <div class="card w-100">
                <div class="card-body">
                    <h4 class="card-title">Create Video</h4>
                    <form id="formvideo" @submit.prevent="checkForm">
                        <div class="row">
                            <div class="col">
                                <label for="title">Title</label>
                                <input type="text" class="form-control" v-model="title" name="title" id="title" placeholder="Title">
                            </div>

                            <div class="col">
                                <label for="description">Description</label>
                                <textarea class="form-control" name="description" id="description" v-model="description" rows="2"></textarea>
                            </div>

                            <div class="col">
                                <label for="url">URL</label>
                                <textarea class="form-control" name="url" id="url" v-model="url" rows="2"></textarea>
                            </div>
                        </div>

                        <div class="row mt-5">
                            <div class="col">
                                <label for="category">Category</label>
                                <input class="form-control" type="text" v-model="category" name="category" id="category">
                            </div>
                            
                            <div class="col">
                                <label for="subcategory">Subcategory</label>
                                <input class="form-control" type="text" v-model="subcategory" name="subcategory" id="subcategory">
                            </div>

                            <div class="col">
                                <label for="author">Author</label>
                                <input class="form-control" type="text" v-model="author" name="author" id="author">
                            </div>
                        </div>
                        
                        <button type="submit" class="btn btn-primary mt-3"
                        @click="$emit('createVideo')"
                        >Create Video</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'CreateVideo',
    components: {

    },
    data() {
        return {
            title: null,
            description: null,
            url: null,
            category:null,
            subcategory:null,
            author:null
        }
    },
    methods: {
        checkForm() {
            axios.post('http://localhost:8181/api/videos/', {
                title: this.title,
                description: this.description,
                url: this.url,
                category: this.category,
                subcategory: this.subcategory,
                author: this.author

            })
            .then( res => console.log(res))
            .catch( err => console.log(err))
        }
    }
}
</script>