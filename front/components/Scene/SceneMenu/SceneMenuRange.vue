<template lang="pug">
.sceneMenuRange-container
  scene-menu-title(:title="title" :description="description")
  input.sceneElement-input(type="range" :min="min" :max="max" step="0.1" v-model="sysValue" @input="$emit('input', sysValue)")
  input.sceneElement-input(v-if="inputField" type="number" v-model="sysValue" @input="$emit('input', sysValue)")
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
      set (value) {
        value = Number(value)
        if (!this.tempValue) {
          this.tempValue = this.$props.value
        }
        if (value < Number(this.$props.min)){
          this.tempValue  = 0
        }
        else if (value > Number(this.max)) {
          this.tempValue  = Number(this.$props.max)
        } else {
          this.tempValue = value
        }
      },
      get () {
        if (this.tempValue === false) {
          this.tempValue = this.$props.value
        }
        return Number(this.tempValue)
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
    isGeneral: {
      default: false,
      type: Boolean
    },
    min: {
      default: '0'
    },
    max: {
      default: '100'
    },
    value: {},
    inputField: {
      default: true
    }
  }
}
</script>

<style lang="css">
</style>
