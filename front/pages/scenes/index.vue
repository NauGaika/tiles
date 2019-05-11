<template lang="pug">
  .scenesCreate-container
    sub-menu(:points="$store.getters['sceneGallery/getSceneCategoryes']" selected="sceneGallery/changeSelectedSceneCategoryId")
    .sceeneGallery-container
      scene-gallery-element(
        v-for="elem in scenes"
        :key="elem.id"
        :id="elem.id"
        :name="elem.name"
        @deleteScene="deleteScene")
      modal-confim-window(v-if="ModalConfimWindow" text="Вы уверены, что хотите удалить данную сцену?" @isOk="deleteSceneConfim" :isConfim="true")
</template>

<script>
import axios from 'axios'
import SubMenu from '~/components/SubMenu/SubMenu.vue'
import SceneGalleryElement from '~/components/Scene/SceneGalleryElement.vue'
export default {
  components: {
    'sub-menu': SubMenu,
    'scene-gallery-element': SceneGalleryElement
  },
  data () {
    return {
      pagesCount: 10,
      pageCurrent: 2,
      scenes: [],
      ModalConfimWindow: false,
      sceneToDel: 0
    }
  },
  computed: {
    scenesGallery () {
      return this.$store.getters['sceneGallery/getСurrentCategoryTitle']
    },
  },
  watch: {
    scenesGallery (val) {
      // console.log(val)
      this.getSceneByCategory(val)
    }
  },
  methods: {
    deleteScene(val) {
      this.ModalConfimWindow = true
      this.sceneToDel = val
    },
    deleteSceneConfim(val) {
      if (val) {
        axios.get(
          '/api/scene/deleteById',
          {
            params: {sceneId: this.sceneToDel}
          }).then(response => {
            this.getSceneByCategory(this.scenesGallery)
        })
      }
      this.ModalConfimWindow = false
      this.sceneToDel = 0
    },
    getSceneByCategory(category) {
      axios.get(
        '/api/scene/getByCategory',
        {
          params: {category}
        }).then(response => {
          // console.log(response.data)
          this.scenes = response.data
      })
    },
  }
}
</script>

<style lang="css">
.sceeneGallery-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.sceeneGallery-pages ul {
  display: flex;
  justify-content: center;
  margin-top: 1em;
}
.sceeneGallery-pages ul li {
  display: flex;
  justify-content: center;
  margin: .3em;
  font-weight: bold;
}
.sceeneGallery-pages ul li:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>
