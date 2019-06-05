<template>
  <div class="d-flex flex-column app-container flex-fill">
    Photo
    <img :src="photoUrl" alt="Smiley face">
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
      photoId: null,
      photoUrl: null,
    };
  },
  created() {
    console.log('Fetch photo');
    // this.photoId: this.$route.params.photoId;
    if (this.photoId === null) {
      console.log('set id');
      this.getInitialId();
      this.getPhoto();
    }
  },
  methods: {
    getInitialId() {
      this.photoId = 1;
    },
    getPhoto() {
      const url = `/api/photos/${this.photoId}`;
      axios.get(url)
        .then((x) => {
          this.photoUrl = x.data.image;
          console.log(this.photoUrl);
        })
        .catch(() => {});
    },
  },
};
</script>
<style>

</style>
