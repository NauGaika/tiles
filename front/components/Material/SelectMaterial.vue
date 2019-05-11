<template lang="pug">
.SelectMaterial-container
  h2 Материалы
  ul
    li(v-for="(i, key) in materialCategory" :class="{'SelectMaterial-active' : i.selected}"
       @click="$store.commit('materialGallery/changeMaterialCategoryId', i.id)") {{i.title}}
  .SelectMaterial-materials
      material-preview-element(v-for="(i, key) in currentMaterials"
                               :element="i"
                               @click="$emit('selectElement', i)")
  span.button(@click="$emit('cancelSelectMaterial')") Отмена
</template>

<script>
import axios from 'axios'
import MaterialPreviewElement from '~/components/Material/MaterialPreviewElement.vue'
export default {
  components: {
    'material-preview-element': MaterialPreviewElement
  },
  data () {
    return {
      currentMaterials: []
    }
  },
  computed: {
    materialCategory () {
      return this.$store.getters['materialGallery/getMaterialCategoryes']
    },
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
          this.currentMaterials = response.data
        })
      }
  },
  mounted() {
    this.getMaterials(this.currentCategoryTitle)
  }
}

</script>

<style lang="css">
.SelectMaterial-container {
  position: fixed;
  z-index: 100;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  /* overflow: scroll; */
  background: rgba(34,57,74, 0.8);
}
.SelectMaterial-container ul li {
  text-shadow: 0 0 .5em rgb(0, 0, 0);
  letter-spacing: .1em;
  transition: .5s;
  border-bottom: 1px solid;
  cursor: pointer;
}
.SelectMaterial-active {
  cursor: default!important;
  border-bottom: none!important;
}
.SelectMaterial-container ul li:hover {
  text-shadow: 0 0 5em rgb(0, 0, 0);
  color: rgb(239,212,159);
}
.SelectMaterial-materials {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
</style>
