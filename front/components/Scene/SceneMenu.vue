<template lang="pug">
div.SceneMenu
  ol.sceneMenuError(v-if="tempError.length > 0")
    li.sceneMenuError-element(v-for="(error, key) in tempError" :key="'error_' + key") {{error}}
  slot
</template>

<script>
export default {
  data () {
    return {
      sysError: []
    }
  },
  computed: {
    tempError () {
      return this.sysError.concat(this.errors)
    }
  },
  props: {
    errors: {
      default: () => [],
      type: Array
    }
  },
  methods: {
    addError (error) {
      for (let e of this.tempError) {
        if (e == error) {
          return
        }
      }
      this.sysError.push(error)
    },
    delError(error) {
      for (let e in this.sysError) {
        if (this.sysError[e] == error) {
          this.sysError.splice(e, 1)
          return
        }
      }
    }
  }
}
</script>

<style lang="css">
.SceneMenu {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 300px;
  width: 450px;
  text-align: center;
  margin-left: 1em;
}
.sceneMenuError {
  border: 2px solid red;
  width: calc(100% - 3em);
  border-radius: 1em;
  padding: 1em;
  list-style: decimal;
  text-align: left;
}
.sceneMenuError-element {
  margin-left: 1em;
}
</style>
