<template lang="pug">
  .MaterialPreviewElement-container(@click="$emit('click', element.id)")
    img(:src="src" v-if="id")
    span.MaterialPreviewElement-article(v-if="id") {{article}}
    span.MaterialPreviewElement-name(v-if="id") {{name}}
    span.MaterialPreviewElement-dimensions(v-if="id") {{dimensions}}
    div.MaterialPreviewElementButton-container(v-if="buttons")
      span.button-small(@click="deleteMaterial") Удалить
      span.button-small.button-fill Редактировать

</template>

<script>
export default {
  props: {
    element: {
      default: () => { return {
          id: 0,
          categoryId: 0,
          article: '',
          name: '',
          dimensions: [0, 0],
        }
      }
    },
    buttons: {
      default: false
    }
  },
  computed: {
    id () {
      if (this.element.id) {
        return this.$props.element.id
      }
      return 0
    },
    categoryId () {
      return this.$props.element.categoryId
    },
    article () {
      return this.$props.element.article
    },
    name () {
      // return this.$props.element.typeName + " " + this.$props.element.produser + " " + this.$props.element.name
      return this.$props.element.name
    },
    dimensions () {
      if (this.element.dimensions) {
        return this.$props.element.dimensions[0] + 'x' + this.$props.element.dimensions[1]
      }
      return ''
    },
    src () {
      return require('~/static/img/material/material_' + this.id + '_preview.png')
    },
  },
  methods: {
    deleteMaterial () {
      this.$emit('deleteMaterial', this.id)
    }
  }
}
</script>

<style lang="css">
.MaterialPreviewElement-container {
  width: 200px;
  /* overflow: hidden; */
  padding: .2em;
  margin: .8em;
  transition: .5s;
  cursor: pointer;
  border-radius: 1em;
}
.MaterialPreviewElement-container:hover {
  background: rgba(122, 122, 122, 0.1);
}

.MaterialPreviewElement-container span {
  width: 200px;
  margin-left: auto;
  margin-right: auto;
}
.MaterialPreviewElement-container img {
  border-radius: 1em;
  width: 100% !important;
  height: auto;
  box-shadow: 0 .2em .2em .1em rgba(0, 0, 0, 0.2);
  transition: 1s;
}
.MaterialPreviewElement-container:hover img {
  box-shadow: 0 .2em .8em .1em rgba(0, 0, 0, 0.2);
}
.MaterialPreviewElement-article {
  display: block;
  text-align: center;
  color: silver;
  margin: .3em 0;
}
.MaterialPreviewElement-article::before {
  content: '['
}
.MaterialPreviewElement-article::after {
  content: ']'
}
.MaterialPreviewElement-name {
  display: block;
  text-align: center;
}
.MaterialPreviewElement-dimensions {
  display: block;
  font-weight: bold;
  text-align: center;
}

.MaterialPreviewElementButton-container span {
  display: block;
  text-align: center;
  padding: .3em 0;
}
</style>
