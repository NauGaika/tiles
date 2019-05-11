<template lang="pug">
  div.subMenu-container
    ul
      li(v-for="point in points")
        span(
          :class="{ 'text-underline' : !point.selected, 'cursor-pointner' : !point.selected }"
          v-on:click="changeSelected(point.id)") {{point.title}}
</template>

<script>
export default {
  data () {
    return {
    }
  },
  props: ['points', 'selected'],
  methods: {
    changeSelected (el) {
      this.$emit('changeCategory')
      this.$store.commit(this.$props.selected, el)
    }
  },
  created () {
  }
}
</script>

<style lang="css">
  .subMenu-container {
    margin-bottom: 2em;
  }
  .subMenu-container ul {
    display: flex;
    justify-content: center;
    font-weight: bold;
  }
</style>
