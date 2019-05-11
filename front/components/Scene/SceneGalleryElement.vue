<template lang="pug">
  .SceneGalleryElement-container
    img.SceneGalleryElement-img(:src="getImgPath()" :alt="name")
    span.SceneGalleryElement-title {{name}}
    .SceneGalleryElement-buttons
      a.button-small.button-stroke(@click="deleteScene") Удалить
      a.button-small.button-fill Редактировать
      a.button-small.button-fill(:href="'/scenes/design/'+id") Выбрать
</template>

<script>
export default {
  props: ['id', 'name'],
  methods: {
    getImgPath () {
      return require('~/static/img/scene/scene_' + this.$props.id + '/scene_preview.png')
    },
    deleteScene () {
      this.$emit('deleteScene', this.$props.id)
    }
  }
}
</script>

<style lang="css">
  .SceneGalleryElement-container{
    max-width: 500px;
    overflow: hidden;
  }
  .SceneGalleryElement-img {
    height: auto;
    border-radius: 1em;
    box-shadow: 0 0 1em .1em rgba(0, 0, 0, 0.5);
    margin: 1em 1em .3em 1em;
    width: calc(100% - 2em);
  }
  .SceneGalleryElement-title {
    text-align: center;
    display: block;
  }
  .SceneGalleryElement-buttons {
    padding: 1em 0;
    text-align: center;
  }
</style>
