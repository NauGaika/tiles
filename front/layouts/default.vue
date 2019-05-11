<template lang="pug">
  .layout-container
    top-menu
    nuxt
</template>

<script>
import TopMenu from "~/components/TopMenu/TopMenu.vue"
export default {
  components: {
    'top-menu': TopMenu
  },
  mounted () {
    this.$store.dispatch('sceneGallery/getSceneCategoryesFromDb')
    this.$store.dispatch('materialGallery/getMaterialCategoryesFromDb')
  }

}
</script>

<style lang="css">
  @import url('https://fonts.googleapis.com/css?family=Roboto');
  * {
    color: rgb(209,182,129);
    font-family: 'Roboto', sans-serif;
    font-size: 18px;
  }
  body {
    background: rgb(54,77,94);
  }
  a {
    text-decoration: none;
    letter-spacing: .3em;
  }
  .layout-container {
    margin: 1em 2em;;
  }
  ul {
    margin: 0;
    padding: 0 1em;
  }
  ul li {
    display: inline;
    margin-right: 2em;
    padding: .2em;
  }
  .text-underline
  {
      text-decoration: underline;
  }
  .cursor-pointner
  {
      cursor: pointer;
  }
  /* Кнопки и их стили */
  .button-small {
    font-size: .8em;
    letter-spacing: 0.1em;
    font-weight: bold;
    padding: .4em;
    border-radius: 1.4em;
    margin: .5em;
    box-shadow: 0 0 .3em .1em rgb(0, 0, 0, 0.3);
    border: 2px solid;
    cursor: pointer;
    transition: .6s;
  }
  .button {
    font-size: 1em;
    letter-spacing: 0.1em;
    font-weight: bold;
    padding: .6em;
    border-radius: 1.4em;
    margin: .5em;
    box-shadow: 0 0 .3em .1em rgb(0, 0, 0, 0.3);
    border: 2px solid;
    cursor: pointer;
    transition: .6s;
    display: inline-block;
  }
  .button-small:hover {
    box-shadow: 0 0 .1em .05em rgb(0, 0, 0, 0.3);
    border-color: rgb(239,212,159);
    color: rgb(239,212,159);
  }
  .button-fill{
    background: rgb(209,182,129);
    color: rgb(54,77,94);
    border-color: rgb(209,182,129);
  }
  .button-fill:hover {
    background: rgb(239,212,159);
    border-color: rgb(239,212,159);
    color: rgb(54,77,94);
  }
  .button-stroke:hover {
    background: rgba(209,182,129, 0.1);
    color: rgb(239,212,159);
  }
  .button-stroke:hover{
    border-color: rgb(239,212,159);
    color: rgb(239,212,159);
  }
  .select-file {
    display: block;
    margin: .5em auto;
  }
  .sceneElement-input {
    display: block;
    margin: .5em auto;
    border-radius: 1em;
    padding: .5em;
    border: 2px solid rgb(209,182,129);;
    text-align: center;
    color: black;
  }
</style>
