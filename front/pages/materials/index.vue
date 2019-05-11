<template lang="pug">
div
  sub-menu(:points="$store.getters['materialGallery/getMaterialCategoryes']"
           selected="materialGallery/changeMaterialCategoryId")
  .materialsGallery-container
    material-preview-element(v-for="(el, pos) in materials" :element="el" :key="pos" :buttons="true" @deleteMaterial="deleteMaterial")
  div.materialsGallery-buttons
    a.button.button-fill(href="materials/create/") Создать новый материал
  modal-confim-window(v-if="ModalConfimWindow" text="Вы уверены, что хотите удалить данный материал?" @isOk="deleteMaterialConfim" :isConfim="true")
</template>
<script>
import axios from 'axios'
import SubMenu from '~/components/SubMenu/SubMenu.vue'
import MaterialPreviewElement from '~/components/Material/MaterialPreviewElement.vue'
export default {
  components: {
    'sub-menu': SubMenu,
    'material-preview-element': MaterialPreviewElement
  },
  data () {
    return {
      pagesCount: 10,
      pageCurrent: 2,
      materials: [],
      curMaterial: 0,
      ModalConfimWindow: false
    }
  },
  computed: {
    currentCategoryTitle () {
      return this.$store.getters['materialGallery/getСurrentCategoryTitle']
    }
  },
  watch: {
    currentCategoryTitle (val) {
      this.getMaterials(val)
    }
  },
  methods: {
    getMaterials(category) {
      axios.get(
        '/api/material/getByCategory',
        {
          params: {category}
        }).then(response => {
        this.materials = response.data
      })
    },
    deleteMaterial (val) {
      this.ModalConfimWindow = true
      this.curMaterial = val
    },
    deleteMaterialConfim (val) {
      if (val) {
        axios.get(
          '/api/material/deleteById',
          {
            params: {materialId: this.curMaterial}
          }).then(response => {
            this.getMaterials(this.currentCategoryTitle)
        })
      }
      this.curMaterial = 0
      this.ModalConfimWindow = false
    }
  }
}
</script>
<style lang="css">
  .materialsGallery-buttons {
    margin-top: 1em;
    text-align: center;
  }
  .materialsGallery-container {
    padding: 1em;
    max-width: 1600px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
