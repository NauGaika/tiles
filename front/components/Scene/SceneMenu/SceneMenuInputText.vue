<template lang="pug">
.SceneMenuInputDimension
  scene-menu-title(:title="title" :description="description")
  input.sceneElement-input(type='text' v-model="sysValue" @input="$emit('input', sysValue)" :placeholder="placeholder")
</template>

<script>
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'

export default {
  components: {
    'scene-menu-title': SceneMenuTitle,
  },
  data () {
    return {
      tempValue: false
    }
  },
  computed: {
    sysValue: {
      get () {
        if (this.tempValue === false) {
          this.tempValue = this.$props.value
        }
        return this.tempValue
      },
      set (val) {
        this.tempValue = val
      }
    }
  },
  props: {
    title: {
      type: String
    },
    description: {
      default: '',
      type: String
    },
    value : {
      default: 0
    },
    placeholder: {
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
</style>
