import * as d3 from "d3"
export default {
  data () {
    return {
      ShowPlanePoints: []
    }
  },
  methods: {
    ShowPlane(point) {
      this.ShowPlanePoints = point.imagePoints
      this.ShowPlaneCreateSVG()
    },
    ShowPlaneCreateSVG () {
      d3.select(".Scene-subcontainer")
        .append('svg')
        .attr('class', 'showPlane')
        .append('g')
        .append('polygon')
        .attr('points', this.ArrayToScale(this.ShowPlanePoints))
    },
    ShowPlaneHide() {
      d3.select(".showPlane").remove()
    }
  }
}
