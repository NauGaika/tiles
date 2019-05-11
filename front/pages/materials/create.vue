<template lang="pug">
.CreateMaterial-container
  scene(ref="scene")
  scene-menu(ref="sceneMenu")
    scene-menu-title(
      title="Создание материала"
      :isGeneral="true")
    scene-menu-select(
      title="Категория"
      description="Выберете категорию к которой отностится материал"
      :elems="this.$store.getters['materialGallery/getMaterialCategoryNames']"
      v-model="templateCategory")
    scene-menu-inputText(
      title="Наименование материала"
      description="Укажите наименование материала."
      v-model="templateName"
      placeholder="Наименование")
    scene-menu-inputText(
      title="Артикль"
      description="Укажите артикль материала. Если артикль не будет указан он сгенерируется автоматически."
      v-model="templateArticle"
      placeholder="Артикль")
    scene-menu-selectMaterialFile(
      title="Текстура материала"
      description="выберете файл с текстурой материала. Желательно, чтобы изображение имело высокое разрышение."
      v-model="templateMaterialFile")
    scene-menu-inputDimension(
      title="Ширина в мм"
      description="Укажите ширину отбразца текстуры"
      v-model="templateWidth")
    scene-menu-inputDimension(
      title="Высота в мм"
      description="Укажите высоту отбразца текстуры"
      v-model="templateHeight")
    scene-menu-inputRange(
      title="Отражающая способность"
      description="Укажите на сколько хорошо материал отражает свет (0-100%)"
      v-model="templateReflect"
      min="0"
      max="100")
    span.button(@click="checkMaterial") Проверить
    span.button.button-fill(@click="appendToDb") Cохранить
</template>

<script>
import axios from 'axios'
import Scene from '~/components/Scene/Scene.vue'
import SceneMenu from '~/components/Scene/SceneMenu.vue'
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'
import SceneMenuRange from '~/components/Scene/SceneMenu/SceneMenuRange.vue'
import SceneMenuSelect from '~/components/Scene/SceneMenu/SceneMenuSelect.vue'
import SceneMenuSelectMaterialFile from '~/components/Scene/SceneMenu/SceneMenuSelectMaterialFile.vue'
import SceneMenuInputDimension from '~/components/Scene/SceneMenu/SceneMenuInputDimension.vue'
import SceneMenuInputText from '~/components/Scene/SceneMenu/SceneMenuInputText.vue'
export default {
  components: {
    'scene': Scene,
    'scene-menu': SceneMenu,
    'scene-menu-title': SceneMenuTitle,
    'scene-menu-select': SceneMenuSelect,
    'scene-menu-selectMaterialFile': SceneMenuSelectMaterialFile,
    'scene-menu-inputDimension': SceneMenuInputDimension,
    'scene-menu-inputText': SceneMenuInputText,
    'scene-menu-inputRange': SceneMenuRange
  },
  data ()
    {
      return {
        templateCategory: undefined,
        templateMaterialFile: undefined,
        templateWidth: 0,
        templateHeight: 0,
        templateReflect: 0,
        templateName: '',
        templateArticle: ''
    }
  },
  watch: {
    templateCategory(el) {
      this.templateCategoryId = this.$store.getters['materialGallery/getMaterialCategoryId'](el)
    }
  },
  methods: {
    // провеяем данные для отправки
    checkData () {
      if (this.templateCategory == "") {
        this.$refs.sceneMenu.addError('Не выбрана категория')
        return
      } else {
        this.$refs.sceneMenu.delError('Не выбрана категория')
      }
      if (this.templateName == "") {
        this.$refs.sceneMenu.addError('Не указано наименование материалами')
        return
      } else {
        this.$refs.sceneMenu.delError('Не указано наименование материалами')
      }
      if (Number(this.templateWidth) <= 0) {
        this.$refs.sceneMenu.addError('Ширина должна быть больше 0 мм')
        return
      } else {
        this.$refs.sceneMenu.delError('Ширина должна быть больше 0 мм')
      }
      if (Number(this.templateHeight) <= 0) {
        this.$refs.sceneMenu.addError('Высота должна быть больше 0 мм')
        return
      } else {
        this.$refs.sceneMenu.delError('Высота должна быть больше 0 мм')
      }
      if (Number(this.templateReflect) < 0) {
        this.$refs.sceneMenu.addError('Отражающая способность не должна быть меньше 0')
        return
      } else {
        this.$refs.sceneMenu.delError('Отражающая способность не должна быть меньше 0')
      }
      if (!(this.templateMaterialFile instanceof File)) {
        this.$refs.sceneMenu.addError('Файл не выбран')
        if (this.templateMaterialFile.type.indexOf('image') == -1) {
          this.$refs.sceneMenu.addError('Файл не является изображением.')
        return
        } else {
          this.$refs.sceneMenu.delError('Файл не является изображением.')
        }
      } else {
        this.$refs.sceneMenu.delError('Файл не выбран')
      }
      return true
    },
    /*Добавляем новый материал в базу*/
    appendToDb () {
      if(this.checkData()) {
        let formData = new FormData()
        formData.append('category', this.templateCategory)
        formData.append('name', this.templateName)
        formData.append('article', this.templateArticle)
        formData.append('file', this.templateMaterialFile)
        formData.append('width', this.templateWidth)
        formData.append('height', this.templateHeight)
        formData.append('reflect', this.templateReflect)
        axios.post('/api/material/create', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          console.log(response)
        })
      }
    },
    /*Проверяем отображение материала перед добавлением*/
    checkMaterial () {
      if (this.checkData()) {
        let sceneId = this.$store.getters['sceneGallery/getDefaultSceneId']
        let formData = new FormData()
        formData.append('width', this.templateWidth)
        formData.append('height', this.templateHeight)
        formData.append('reflect', this.templateReflect)
        formData.append('file', this.templateMaterialFile)
        formData.append('sceneId', sceneId)
        axios.post('/api/material/check', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(response => {
          this.$refs.scene.ResizeImgSrc = response.data
        })
      }
    }
  },
  mounted () {
  }
}
</script>

<style lang="css">
.CreateMaterial-container {
  display: flex;
  align-content: stretch;
  align-items: center;
}
</style>
