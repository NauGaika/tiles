// import opencv from "opencv"
import * as d3 from "d3"

export default {
  data () {
    return {
      SelectPlanePoints: [],
      SelectPlanePolygons: false,
    }
  },
  watch: {
    ResizeKoef (val) {
      this.SelectPlaneChangeScale()
    }
  },
  methods: {
    createSelectPolygons(points) {
      let self = this
      this.SelectPlanePoints = points
      console.log(points)
      let svgElement = d3.select('.Scene-subcontainer').append('svg').attr('class', 'SelectPlane').append('g')
      this.SelectPlanePolygons = svgElement.selectAll('polygon').data(this.SelectPlanePoints).enter().append('polygon').attr('points', d => this.ArrayToScale(d[0]))
                                  .on("click", d => {
                                    self.$emit('selectPolygon', d[1])
                                  })
    },
    hideSelectPolygons() {
      d3.selectAll('svg').select('.SelectPlane').remove()
    },
    SelectPlaneChangeScale() {
      if (this.SelectPlanePolygons) {
        this.SelectPlanePolygons.attr('points', d => this.ArrayToScale(d[0]))
      }
    }
  },
  beforeDestroy () {
    this.hideSelectPolygons()
  }
}
