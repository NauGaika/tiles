<template lang="pug">
.SceneMenuElement-container
  scene-menu-title(:title="title" :description="description")
  img.SceneMenuElement-materialPreview(v-if="sysValue" ref='materialPreview')
  scene-menu-select-file(v-model="sysValue" @input="getImage()")
</template>

<script>
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'
import SceneMenuSelectFile from '~/components/Scene/SceneMenu/SceneMenuSelectFile.vue'

export default {
  components: {
    'scene-menu-title': SceneMenuTitle,
    'scene-menu-select-file': SceneMenuSelectFile
  },
  data () {
    return {
      sysValue: undefined
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
    }
  },
  methods: {
    getImage() {
      this.$emit('input', this.sysValue)
      let reader = new FileReader()
      reader.onloadend = () => {
        let image = new Image()
        let src = reader.result
        image.src = reader.result
        image.onload = () => {
          console.log(image.width)
          this.$refs.materialPreview.src = image.src
        }
      }
      if(this.sysValue) {
        reader.readAsDataURL(this.sysValue)
      }
      else {
        this.$refs.materialPreview.src = ''
      }
    }
  }
}
</script>

<style lang="css">
.SceneMenuElement-container img {
  margin: 0 auto;
  display: block;
  border: 2px solid;
  border-radius: 1em;
  width: 240px;
  height: auto;
  box-shadow: 0 .3em .3em .1em rgba(0, 0, 0, 0.3)
}
</style>
