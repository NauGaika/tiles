<template lang="pug">
  div.TopMenu-container
    img(src="~/static/img/general/logo.png").TopMenu-logo
    ul
      li(v-for="point in menuPoints")
        a(:href="point.url") {{point.name}}
</template>

<script>
export default {
  data ({ req }) {
    return {
      menuPoints: [
        {
          name: 'Создание сцены',
          url: '/scenes/create'
        },
        {
          name: 'Ассортимент материалов',
          url: '/materials'
        },
        {
          name: 'Галерея сцен',
          url: '/scenes'
        }
      ]
    }
  }
}
</script>

<style lang="css" scoped="scoped">
  .TopMenu-container ul li a {
    display: inline-block;
    margin-top: .3em;
  }
  .TopMenu-container ul li a:hover {
    text-decoration: underline;
  }
  .TopMenu-container {
    display: flex;
    align-items: flex-end;
    margin-bottom: 2em;
  }
  .TopMenu-logo {
    height: 3em;
  }
</style>
