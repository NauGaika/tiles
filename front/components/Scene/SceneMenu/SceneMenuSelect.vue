<template lang="pug">
.SceneMenuElement-container
  scene-menu-title(:title="title" :description="description")
  input.SceneMenuElement-input(v-if="selectInput" :list="title" name="selectElement" v-model="value"  @input="$emit('input', value)")
  datalist(:id="title")
    option(v-for="(point, key) in elems" :value="point")
  select.SceneMenuElement-input(v-if="!selectInput" v-model="value" @change="$emit('input', value)")
    option(v-for="(point, key) in elems" :key="point + key") {{point}}
</template>

<script>
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'

export default {
  components: {
    'scene-menu-title': SceneMenuTitle,
  },
  data () {
    return {
      value: this.$props.elems[0]
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
    elems: {
      default: [],
      type: Array
    },
    selectInput: {
      default: false,
      type: Boolean
    }
  },
  mounted () {
    this.$emit('input', this.value)
  }
}
</script>

<style lang="css">
.SceneMenuElement-input {
  width: calc(100% - 2em);
  height: 1.6em;
  text-align: center;
  font-size: 1.2em;
  color: black;
  border-radius: 1em;
  border: 1px solid;
  margin: 1em;
  background: white;
}
.SceneMenuElement-input option {
  height: 1.4em;
  color:black;
  text-align: center;
}
</style>
