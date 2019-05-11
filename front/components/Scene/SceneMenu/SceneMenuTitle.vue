<template lang="pug">
  .SceneMenuTitle-container
    span.SceneMenuTitle-title(:class="{'SceneMenuTitle-general' : isGeneral}") {{title}}
    span.SceneMenuTitle-description(v-if="Boolean(description)") {{description}}
</template>

<script>
export default {
  props: {
    title: {
      type: String
    },
    description: {
      default: '',
      type: String
    },
    isGeneral: {
      default: false,
      type: Boolean
    }
  }
}
</script>

<style lang="css">
.SceneMenuTitle-container {
  margin-top: 1em;
  padding: 0 1em;
}
.SceneMenuTitle-general {
  font-size: 1.4em;
  margin-top: -1em;
}
.SceneMenuTitle-container span {
  display: block;
  text-align: center;
  letter-spacing: .17em;
}
.SceneMenuTitle-description {
  color: Silver;
  font-size: .8em;
  margin: .4em 0;
}
</style>
