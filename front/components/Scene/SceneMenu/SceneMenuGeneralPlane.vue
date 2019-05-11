<template lang="pug">
li.SceneMenuGeneralPlane-container(
  @mouseout="$emit('mouseout')"
  @mouseover="$emit('mouseover')") Плоскость
  span.button-small(@click="$emit('delete')") Удалить
  span.button-small.button-fill(@click="$emit('edit')") Редактировать
</template>

<script>
export default {
  data () {
    return {
      points: []
    }
  }
}
</script>

<style lang="css">
.SceneMenuGeneralPlane-container {
  margin-bottom: 1em;
  font-weight: bold;
  cursor: pointer;
}
</style>
