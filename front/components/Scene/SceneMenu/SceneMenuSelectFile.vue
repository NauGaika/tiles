<template lang="pug">
div
  scene-menu-title(:title="title" :description="description")
  input.button.select-file.button-fill(type="file" ref="file" accept="image/*,image/jpeg" @change="$emit('input', getFile())")
</template>

<script>
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'

export default {
  components: {
    'scene-menu-title': SceneMenuTitle,
  },
  props: {
    isGeneral: {
      default: false,
      type: Boolean
    },
    title: {
      default: "",
      type: String
    },
    description: {
      default: '',
      type: String
    }
  },
  methods: {
    getFile () {
      if ( this.$refs.file.files){
        return this.$refs.file.files[0]
      }
      return undefined
    }
  }
}
</script>

<style lang="css">
</style>
