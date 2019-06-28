<template>
  <div>
    <div class="d-flex flex-row justify-content-center">
      <div class="previous color-white large-font" @click="getPreviousPhoto()">
        Previous
      </div>
      <div class="color-white large-text">
        {{ photoIndex + 1 }} / {{ photos.length }}
      </div>
      <div class="next color-white large-font" @click="getNextPhoto()">
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

export default {
  name: 'App',
  data() {
    return {
      photoIndex: 0,
      photoUrl: null,
      photos: [],
      loadingImg: true,
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
          this.setPhoto();
        });
    },
    getNextPhoto() {
      if (this.photoIndex !== this.photos.length - 1) {
        this.photoIndex += 1;
        this.setPhoto();
      }
    },
    getPreviousPhoto() {
      if (this.photoIndex !== 0) {
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

.center-fit {
  max-width: 95%;
  max-height: 95vh;
  margin: auto;
}

.color-white {
  color: white;
}

.image-wrapper {
  display: grid;
}

.large-font {
  font-size: large;
}

.next {
  margin-left: 20px;
  cursor: pointer;
  padding: 0 10 0 10;
}

.previous {
  margin-right: 20px;
  cursor: pointer;
  padding: 0 10 0 10;
}
</style>
