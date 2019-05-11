<template lang="pug">
.ScenesDesign-conteiner
  scene(ref="scene" :img="imgSrc"
        @selectPolygon="selectPolygon($event)")
  scene-menu
    scene-menu-title(
      title="Работа со сценой"
      description="Выберете подходящий материал и наложите на соовтетствующую поверхность"
      :isGeneral="true")
    scene-menu-select-material(@selectMaterial="selectMaterial" :element="curMaterial")
    transition(name="SelectMaterialTransion")
      select-material(v-if="isSelectMaterial"
                      @cancelSelectMaterial="isSelectMaterial=false"
                      @selectElement="materialSelected")
</template>

<script>
import axios from 'axios'
import Scene from '~/components/Scene/Scene.vue'
import SceneMenu from '~/components/Scene/SceneMenu.vue'
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'
import SceneMenuRange from '~/components/Scene/SceneMenu/SceneMenuRange.vue'
import SceneMenuSelect from '~/components/Scene/SceneMenu/SceneMenuSelect.vue'
import SceneMenuSelectMaterialFile from '~/components/Scene/SceneMenu/SceneMenuSelectMaterialFile.vue'
import SceneMenuSelectFile from '~/components/Scene/SceneMenu/SceneMenuSelectFile.vue'
import SceneMenuInputDimension from '~/components/Scene/SceneMenu/SceneMenuInputDimension.vue'
import SceneMenuGeneralPlane from '~/components/Scene/SceneMenu/SceneMenuGeneralPlane.vue'
import SceneMenuSelectMaterial from '~/components/Scene/SceneMenu/SceneMenuSelectMaterial.vue'
import SelectMaterial from '~/components/Material/SelectMaterial.vue'

export default {
  components: {
    'scene': Scene,
    'scene-menu': SceneMenu,
    'scene-menu-title': SceneMenuTitle,
    'scene-menu-select': SceneMenuSelect,
    'scene-menu-selectMaterialFile': SceneMenuSelectMaterialFile,
    'scene-menu-selectFile': SceneMenuSelectFile,
    'scene-menu-inputDimension': SceneMenuInputDimension,
    'scene-menu-inputRange': SceneMenuRange,
    'scene-menu-general-plane': SceneMenuGeneralPlane,
    'scene-menu-select-material': SceneMenuSelectMaterial,
    'select-material': SelectMaterial
  },
  data () {
    return {
      id: this.$route.params.id,
      curImg: undefined,
      isSelectMaterial: false,
      curMaterial: {},
      points: [],
      currentSession: false
    }
  },
  validate ({ params }) {
    this.id = params.id
    return true
  },
  computed: {
    imgSrc () {
      if (!this.curImg){
        return require('~/static/img/scene/scene_' + String(this.id) + '/scene.png')
      } else {
        return this.curImg
      }
    }
  },
  methods: {
    selectMaterial () {
      this.isSelectMaterial = true
    },
    materialSelected (el) {
      this.isSelectMaterial = false
      this.curMaterial = el
    },
    selectPolygon(d) {
      this.addTexture(d)
    },
    addTexture(poligonId) {
      let self = this
      this.id
      this.currentSession
      poligonId
      this.curMaterial
      if (this.curMaterial.id) {
        let formData = new FormData()
        formData.append('sceneId', this.id)
        formData.append('poligonId', poligonId)
        formData.append('materialId', this.curMaterial.id)
        formData.append('session', this.currentSession)
        axios.post('/api/scene/design', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          this.currentSession = response.data
          let curImg = this.currentSession + '.png?' + Math.round(Math.random() * 10000)
          curImg = '/img/session/' + curImg
          self.$refs.scene.DesignShowImg(curImg)
        })
      }
    }
  },
  mounted() {
    axios.get('/api/scene/getAllPlanePoints', {
      params: {
        id: this.id
      }
    }).then(response => {
      this.points = response.data
      this.$refs.scene.createSelectPolygons(this.points)
    })
  }
}
</script>

<style lang="css">
.ScenesDesign-conteiner {
  display: flex;
  align-content: stretch;
  align-items: center;
}
.SelectMaterialTransion-enter-active, .SelectMaterialTransion-leave-active {
  transition: opacity .5s;
}
.SelectMaterialTransion-enter, .SelectMaterialTransion-leave-to {
  opacity: 0;
}
</style>
