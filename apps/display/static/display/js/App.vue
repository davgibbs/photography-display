<template>
  <div class="d-flex flex-column app-container flex-fill">
    <div @click="getNextPhoto()">
      Next
    </div>
    <div @click="getPreviousPhoto()">
      Previous
    </div>
    <img :src="photoUrl" alt="Chosen photo">
  </div>
</template>
<script>
const axios = require('axios');

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: 'App',
  data() {
    return {
      photoIndex: null,
      photoUrl: null,
      photos: [],
    };
  },
  created() {
    this.getPhotos();
  },
  methods: {
    setPhoto() {
      this.photoUrl = this.photos[this.photoIndex].image;
    },
    getPhotos() {
      const url = '/api/photos';
      axios.get(url)
        .then((x) => {
          this.photos = x.data;
          this.photoIndex = 0;
          this.setPhoto();
        });
    },
    getNextPhoto() {
      if (this.photoIndex === this.photos.length - 1) {
        this.photoIndex = this.photos.length - 1;
        this.setPhoto();
      } else {
        this.photoIndex += 1;
        this.setPhoto();
      }
    },
    getPreviousPhoto() {
      if (this.photoIndex === 0) {
        this.photoIndex = 0;
        this.setPhoto();
      } else {
        this.photoIndex -= 1;
        this.setPhoto();
      }
    },
  },
};
</script>
<style>

</style>
