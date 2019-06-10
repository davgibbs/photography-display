<template>
  <div>
    <div class="d-flex flex-row justify-content-center">
      <div class="previous" @click="getPreviousPhoto()">
        Previous
      </div>
      <div class="photo-count">
        {{ photoIndex + 1 }} / {{ photos.length }}
      </div>
      <div class="next" @click="getNextPhoto()">
        Next
      </div>
    </div>
    <div class="d-flex flex-row justify-content-center">
      <div class="image-wrapper">
        <img :src="photoUrl" alt="Chosen photo" class="center-fit">
      </div>
    </div>
  </div>
</template>
<script>
require('bootstrap/dist/css/bootstrap.min.css');
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
body {
  background-color:black;
}

.next {
  margin-left: 20px;
  color: white;
  cursor: pointer;
  padding: 0 10 0 10;
}

.previous {
  margin-right: 20px;
  color: white;
  cursor: pointer;
  padding: 0 10 0 10;
}

.photo-count {
  color: white;
}

.image-wrapper {
  display: grid;
}

.center-fit {
  max-width: 95%;
  max-height: 95vh;
  margin: auto;
}
</style>
