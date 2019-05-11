<template lang="pug">
  .ModalConfimWindow-container
    .ModalConfimWindow-block
      .ModalConfimWindow-text {{ text }}
      .ModalConfimWindow-controller(v-if="isConfim")
        span.button-small.button-fill(@click="$emit('isOk', true)") Подтвердить
        span.button-small(@click="$emit('isOk', false)") Отменить
</template>
<script>
export default {
  props: {
    text: {
      default: ''
    },
    isConfim: {
      default: false
    }
  }
}
</script>
<style>
  .ModalConfimWindow-container {
    display: flex;
    position: absolute;
    background: rgba(0, 0, 0, 0.2);
    left: 0;
    right: 0;
    bottom: 0;
    top:0;
  }
  .ModalConfimWindow-block {
    display: block;
    margin: auto;
    background: rgb(54,77,94);
    padding: 1em;
    border-radius: 1em;
    border: 2px solid;
  }
  .ModalConfimWindow-controller {
    text-align: center;
  }
  .ModalConfimWindow-controller span {
    margin: .5em !important;
  }
  .ModalConfimWindow-text {
    padding-bottom: 2em;
  }
</style>
