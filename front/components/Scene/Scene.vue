<template lang="pug">
.Scene-container(ref="divElem")
  .Scene-subcontainer(ref="imgElem" :style="{'background-image': 'url('+ResizeImgSrc+')' , 'min-height': height + 'px'}")
  .Scene-preview(v-if="previewUrl" ref="imgPreview" :style="{'background-image': 'url('+previewUrl+')' , 'min-height': height + 'px'}")
</template>

<script>
import * as d3 from "d3"
import ResizeMixin from "~/mixins/scene/ResizeMixin.js"
import CreatePlaneMixin from "~/mixins/scene/CreatePlaneMixin.js"
import ShowPlaneMixin from "~/mixins/scene/ShowPlaneMixin.js"
import EditPlaneMixin from "~/mixins/scene/EditPlaneMixin.js"
import SelectPlaneMixin from "~/mixins/scene/SelectPlaneMixin.js"
import DesignMixin from "~/mixins/scene/DesignMixin.js"
export default {
  mixins: [ResizeMixin, CreatePlaneMixin, ShowPlaneMixin, EditPlaneMixin, SelectPlaneMixin, DesignMixin],
  data () {
    return {
      isEdit: false,
      EditKey: -1,
      previewUrl: ''
    }
  },
  methods: {
    addPlane () {
      return this.sysPlanePoints.map((el) => el.slice(0,2))
    },
    hideAll () {
      d3.select('.Scene-subcontainer').selectAll('svg').remove()
    }
  }
}

</script>

<style lang="css">
/* .Scene-container {
  min-width: 70%;
} */
.Scene-container {
  position: relative;
  border: 2px solid;
  border-radius: 1em;
  overflow: hidden;
  box-shadow: 0 .3em .3em .3em rgba(0, 0, 0, 0.1);
  flex-grow: 2;
  min-width: 300px;
  display: flex;
  align-items: flex-start;
  background-repeat: no-repeat;
}
.Scene-subcontainer{
  display: block;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-position: center;
  transition-property: background-size;
}
.Scene-preview {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.Scene-container svg {
  position: absolute;
  top: 0;
  left: 0;
  overflow: visible;
  width: 100%;
  height: 100%;
}
/* отображение плоскости временно */
polygon, line {
  stroke: rgba(0, 255, 0, 0.5);
  stroke-width: 3;
  fill: rgba(0, 255, 0, 0.2);
}
.Scene-PlaneAddNew line {
  display: block;
  stroke: rgba(0, 255, 0, 0.5);
}
.Scene-PlaneAddNew text {
  fill: rgba(255, 0, 0, 1);
  text-shadow: 1px 1px 2px black, 0 0 1em red;
  font-size: 1em;
}
.PointCirce {
  r: 6px;
  stroke: rgba(0, 255, 0, 0.8);
  stroke-width: 2;
  fill: rgba(255, 0, 0, 0.8);
  cursor: move;
}
/* .SVG-text {
  stroke:
} */
.SelectPlane {
  z-index: 10;
}
.SelectPlane polygon {
  fill: rgba(0, 255, 0, 0);
  stroke: rgba(0, 255, 0, 0);
  cursor: pointer;
  transition: .5s;

}
.SelectPlane polygon:hover {
  fill: rgba(0, 255, 0, 0.3);
  stroke: rgba(0, 255, 0, 0.8);
  cursor: pointer;

}
.DesignShowNewImg {
  display: block;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 9;
  transition: 0.5s;
  width: 100%;
  height: 100%;
}
</style>
