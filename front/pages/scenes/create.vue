<template lang="pug">
.ScenesCreate-conteiner
  scene(ref="scene" :img="sceneImgGeneral" :tempRealWidth="tempRealWidth" :tempRealHeight="tempRealHeight" :scale="resizeKoef")
  scene-menu(v-show="createStage==0" :errors="errors")
    scene-menu-title(
      title="Создание сцены"
      description="Для начала выберем файл будущей сцены"
      :isGeneral="true")
    scene-menu-inputText(
      title="Наименование сцены"
      description="Укажите наименование сцены."
      v-model="sceneName"
      placeholder="Наименование")
    scene-menu-select(
      title="Категория"
      description="Выберете категорию к которой отностится сцена."
      :elems="this.$store.getters['sceneGallery/getSceneCategoryesNames']"
      v-model="sceneCategory")
    scene-menu-selectFile(v-model="sceneImgGeneral")
    span.button.button-fill(@click="checkStage(0)") Далее
  scene-menu(v-show="createStage==1" :errors="errors")
    scene-menu-title(
      title="Создание основных плоскостей"
      description="Основные плоскости - стены, полы, грани колонн."
      :isGeneral="true")
    ol.SceneMenu-generalPlanes
      scene-menu-general-plane(
        v-for="(el, key) in sceneGeneralPlanes"
        :key="'scene_pane_' + key"
        :eldata="el"
        @delete="deletePlane(key)"
        @edit="EditPlane(key)"
        @mouseout="ShowPlaneHide()"
        @mouseover="ShowPlane(el)"
        )
    span.button.button-fill(@click="checkStage(1)") Добавить плоскость
    .SceneMenu-finishButton
      span.button(@click="createStage -= 1") Назад
      span.button.button-fill(@click="checkStage(3)") Далее
  scene-menu(v-if="createStage==2" :errors="errors")
    scene-menu-title(
      title="Создание плоскости"
      description="Для создания плоскости укажите ее реальные размеры"
      :isGeneral="true"
      )
    scene-menu-title(
      title="Размеры плоскости"
      description="Укажите реальные размеры плоскости. И разместите плоскость на сцене.")
    scene-menu-inputDimension(title="Ширина мм" placeholder="1000" v-model="tempRealWidth")
    scene-menu-inputDimension(title="Высота мм" placeholder="1000" v-model="tempRealHeight")
    scene-menu-selectFile(title="Маска плоскости" description="Выберете файл маску для плоскости." v-model="currentMask")
    scene-menu-title(title="Масштаб" description="Если плоскость выходит за рамки изображение - измените масштаб")
    scene-menu-inputRange(max="5" min="1" :inputField='false' v-model="resizeKoef")
    .SceneMenu-finishButton
      span.button.button-stroke(@click="checkStage(6)") Отмена
      span.button.button-fill(@click="checkStage(2)") {{isEditPlane}}
  scene-menu(v-show="createStage==4" :errors="errors")
    scene-menu-title(
      title="Добавление слоев света и тени."
      description="Выберете файлы для добавления света и тени"
      :isGeneral="true"
      )
    scene-menu-selectFile(title="Файл со светом" description="Выберете файл со светом." v-model="layaerLight")
    scene-menu-selectFile(title="Файл с тенями" description="Выберете файл с тенями." v-model="layaerShadow")
    .SceneMenu-finishButton
      span.button.button-stroke(@click="createStage = 1") Назад
      span.button.button-fill(@click="checkStage(4)") Далее
  scene-menu(v-show="createStage==5" :errors="errors")
    scene-menu-title(
      title="Завершение"
      description="Перед созданием проверьте правильность отображения сцены. Возможно стоит внести коррективы."
      :isGeneral="true"
      )
    span.button.button-stroke(@click="checkStage(5)") Проверить
    .SceneMenu-finishButton
      span.button.button-stroke(@click="checkStage(8)") Назад
      span.button.button-fill(@click="checkStage(7)") Добавить
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
import SceneMenuInputText from '~/components/Scene/SceneMenu/SceneMenuInputText.vue'

export default {
  data () {
    return {
      createStage: 0,
      sceneCategory: undefined,
      sceneImgGeneral: undefined,
      tempRealWidth: 3500,
      tempRealHeight: 2700,
      resizeKoef: 1,
      currentMask: false,
      sceneGeneralPlanes: [],
      errors: [],
      layaerLight: false,
      layaerShadow: false,
      isEdit: false,
      sceneName: ''
    }
  },
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
    'scene-menu-inputText': SceneMenuInputText
  },
  computed: {
    isEditPlane() {
      let res = 'Добавить'
      if (this.$refs.scene) {
        res = this.$refs.scene.isEdit ? 'Изменить' : 'Добавить'
      }
      return res
    }
  },
  methods: {
    ShowPlaneHide () {
      this.$refs.scene.ShowPlaneHide()
    },
    ShowPlane (p) {
      this.$refs.scene.ShowPlane(p)
    },
    deletePlane (key) {
      this.sceneGeneralPlanes.splice(key, 1)
    },
    addError(error) {
      for (let e of this.errors) {
        if (e == error) {
          return
        }
      }
      this.errors.push(error)
    },
    delError(error) {
      for (let e in this.errors) {
        if (this.errors[e] == error) {
          this.errors.splice(e, 1)
          return
        }
      }
    },
    EditPlane (p) {
      this.ShowPlaneHide()
      this.$refs.scene.EditPlane(this.sceneGeneralPlanes[p], p)
      this.createStage = 2
    },
    checkStage(stage) {
      let nextStage = this.createStage
      switch (stage) {
        case 0:
        // При попытке перейти к созданию плоскостей
          if (this.checkStage_0()){
            this.createStage = 1
          }
          break
        case 1:
        // При попытке добавить плоскость
          this.$refs.scene.ShowPlaneHide()
          this.$refs.scene.CreatePlane()
          this.createStage = 2
          break
        case 2:
        // При нажатии создать плоскость

          this.checkStage_2()
          break
        case 3:
        // При попытке перейти к добавлению света и тени.
          if (this.checkStage_3())
          {
            this.createStage = 4
          }
          break
        case 4:
        // При попытке перейти к добавлению света и тени.
          this.checkStage_4()
          break
        case 5:
        // При попытке проверить нашу сцену
          this.checkStage_5()
          break
        case 6:
        // При попытке отменить доавбление плоскости
          this.$refs.scene.hideAll()
          this.createStage = 1
          break
        case 7:
          this.sendDataToDb()
          break
        case 8:
          this.createStage -= 1
          this.$refs.scene.previewUrl = ""
          // this.$refs.scene.ResizeImgSrc = '/img/scene/scene_8/scene.png'
          break
      }
    },
    sendDataToDb () {
      this.sceneCategory
      this.layaerLight
      this.layaerShadow
      this.sceneGeneralPlanes
      this.sceneImgGeneral
      let formData = new FormData()
      formData.append('category', this.sceneCategory)
      formData.append('light', this.layaerLight)
      formData.append('shadow', this.layaerShadow)
      formData.append('img', this.sceneImgGeneral)
      formData.append('name', this.sceneName)
      for (let i in this.sceneGeneralPlanes) {
        let plane = this.sceneGeneralPlanes[i]
        formData.append('points_'+ String(i), JSON.stringify(plane.imagePoints))
        formData.append('realWidth_'+ String(i), plane.realWidth)
        formData.append('realHeight_'+ String(i), plane.realHeight)
        formData.append('mask_'+ String(i), plane.mask)
      }
      axios.post('/api/scene/create', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        console.log(response)
      })

    },
    checkImgResolution(img, testImg) {
      return new Promise((resolve, reject) => {
        let imgRes = [0, 0]
        let testImgRes = [0, 0]
        let reader = new FileReader()
        reader.readAsDataURL(img)
        reader.onload = () => {
          let imgObj = new Image()
          imgObj.src = reader.result
          imgObj.onload = () => {
            imgRes = [imgObj.width, imgObj.height]
            // reader_2
            reader.onload = () => {
              imgObj = new Image()
              imgObj.src = reader.result
              imgObj.onload = () => {
                testImgRes = [imgObj.width, imgObj.height]
                if (imgRes[0] == testImgRes[0] && imgRes[1] == testImgRes[1]) {
                  resolve(imgRes.concat(testImgRes))
                } else {
                  reject(imgRes.concat(testImgRes))
                }
              }
            }
            reader.readAsDataURL(testImg)
          }
        }
      })

    },
    checkStage_0() {
      if (typeof this.sceneImgGeneral == 'object') {
        this.delError('Выберете файл')
        return true
      } else {
        this.addError('Выберете файл')
      }
    },
    checkStage_1() {
      return true
    },
    checkStage_2() {
      let points = this.$refs.scene.addPlane()
      let mask = this.currentMask
      let realDimension = [this.tempRealWidth, this.tempRealHeight]
      if (mask) {
        this.delError('Не добавлена маска для слоя.')
        this.checkImgResolution(mask, this.sceneImgGeneral).then(
          result => {
            this.delError('Разрышения маски не соответствует разрышению сцены')
            let objToPush = {
                          imagePoints: points,
                          realWidth: this.tempRealWidth,
                          realHeight: this.tempRealHeight,
                          mask
                        }
            if (this.$refs.scene.isEdit){
              this.$refs.scene.isEdit = false
              this.$set(this.sceneGeneralPlanes, this.$refs.scene.EditKey, objToPush)
            } else {
              this.sceneGeneralPlanes.push(objToPush)
            }
            this.resizeKoef = 1
            this.currentMask = false
            this.$refs.scene.hideAll()
            this.createStage = 1
          },
          error => {
            this.addError('Разрышения маски не соответствует разрышению сцены')
          })
      } else {
        this.addError('Не добавлена маска для слоя.')
      }
    },
    checkStage_3() {
      if (this.sceneGeneralPlanes.length > 0)
      {
        this.delError('Необходимо добавить хотя бы одну рабочую плоскость.')
        return true
      } else {
        this.addError('Необходимо добавить хотя бы одну рабочую плоскость.')
      }
    },
    checkStage_4() {
      if (this.layaerLight)
      {
        this.delError('Необходимо добавить слой со светом.')
        if (this.layaerShadow){
          this.delError('Необходимо добавить слой с тенями.')

          this.checkImgResolution(this.layaerLight, this.sceneImgGeneral).then(
            result => {
              this.delError('Разрышение изображения света на соответствует изображению сцены.')
              this.checkImgResolution(this.layaerShadow, this.sceneImgGeneral).then(
                result => {
                  this.delError('Разрышение изображения теней на соответствует изображению сцены.')
                  this.createStage = 5
                },
                error => {
                  this.addError('Разрышение изображения теней на соответствует изображению сцены.')
                }
              )
            },
            error => {
              this.addError('Разрышение изображения света на соответствует изображению сцены.')
            })
        } else {
          this.addError('Необходимо добавить слой с тенями.')
        }
      } else {
        this.addError('Необходимо добавить слой со светом.')
      }
    },
    checkStage_5() {
      let formData = new FormData()
      formData.append('light', this.layaerLight)
      formData.append('shadow', this.layaerShadow)
      formData.append('img', this.sceneImgGeneral)
      for (let i in this.sceneGeneralPlanes) {
        let plane = this.sceneGeneralPlanes[i]
        formData.append('points_'+ String(i), JSON.stringify(plane.imagePoints))
        formData.append('realWidth_'+ String(i), plane.realWidth)
        formData.append('realHeight_'+ String(i), plane.realHeight)
        formData.append('mask_'+ String(i), plane.mask)
      }
      axios.post('/api/scene/check', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        this.$refs.scene.previewUrl = response.data
      })
    }
  },
}
</script>

<style lang="css">
.ScenesCreate-conteiner {
  display: flex;
  align-content: stretch;
  align-items: center;
}
.SceneMenu-generalPlanes {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
</style>
