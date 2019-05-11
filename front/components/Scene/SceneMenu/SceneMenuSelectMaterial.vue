<template lang="pug">
.SceneMenuElement-container
  scene-menu-title(title="Выберете материал" description="Выберете материал, который хотите наложить")
  span.button.button-fill(@click="$emit('selectMaterial')") Выбрать материал
  material-preview(:element="element")
</template>

<script>
import SceneMenuTitle from '~/components/Scene/SceneMenu/SceneMenuTitle.vue'
import MaterialPreviewElement from '~/components/Material/MaterialPreviewElement.vue'

export default {
  components: {
    'scene-menu-title': SceneMenuTitle,
    'material-preview': MaterialPreviewElement,
  },
  data () {
    return {
    }
  },
  props: {
    element: {
      default: () => { return {
                                id: 10,
                                categoryId: 0,
                                article: 'test',
                                name: 'test',
                                dimensions: [450, 450],
                              }
                     }
    }
  },
  methods: {
  }
}
</script>

<style lang="css">
.SceneMenuElement-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
