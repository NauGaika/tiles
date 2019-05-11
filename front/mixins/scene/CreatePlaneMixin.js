import * as d3 from "d3"
import solve from "~/plugins/numeric-solve.js"

export default {
  data () {
    return {
      sysPlanePoints : [],
      sysStartPlanePoints: [],
      SvgPoint: undefined,
      CreatePlanePointsElems: undefined,
      CreatePlanePointsDefTilesWidth: 250,
      CreatePlanePointsDefTilesHeight: 250,
      StartResizeKoef: 1
    }
  },
  props: {
    tempRealWidth: {},
    tempRealHeight: {}
  },
  computed: {
    CreatePlaneTilesCountWidth() {
      let count = Number(this.tempRealWidth / this.CreatePlanePointsDefTilesWidth)
      if (count > 200) {
        return 0
      }
      return count
    },
    CreatePlaneTilesCountHeight() {
      let count = Number(this.tempRealHeight / this.CreatePlanePointsDefTilesHeight)
      if (count > 200) {
        return 0
      }
      return count
    },
  },
  watch: {
    tempRealWidth (val) {
      this.CreatePlaneChangeGrid()
    },
    tempRealHeight (val) {
      this.CreatePlaneChangeGrid()
    },
    ResizeKoef () {
      if (this.PlaneIsShow) {
        this.CreatePlaneSetPointParams()
        this.CreatePlaneTransformed()
      }
    },
    scale () {
      if (this.PlaneIsShow) {
        this.CreatePlaneSetPointParams()
      }
    }
  },
  methods: {
    PointToScale(pos, scale=true, koef=false) {
      let elem = pos
      if (typeof pos == 'number') {
        elem = this.sysPlanePoints[pos]
      }
      if (scale) {
        scale = this.scale
      } else {
        scale = 1
      }
      let resizeKoef = typeof koef == "number" ? koef : this.ResizeKoef
      let dx = (this.width - this.width / scale ) / 2
      let dy = (this.height - this.height / scale ) / 2

      let x = resizeKoef / scale * elem[0] + dx
      let y = resizeKoef / scale * elem[1] + dy
      return [Math.round(x, 3), Math.round(y, 3)]
    },
    ArrayToScale(arr, scale=true, koef=false) {
      return arr.map((el) => this.PointToScale(el, scale, koef))
    },
    PointOfScale(pos) {
      let elem = pos
      if (typeof pos == 'number') {
        elem = this.sysPlanePoints[pos]
      }
      let dx = (this.width - this.width / this.scale ) / 2
      let dy = (this.height - this.height / this.scale ) / 2

      let x = (elem[0] - dx) / this.ResizeKoef * this.scale
      let y = (elem[1] - dy) / this.ResizeKoef * this.scale
      return [Math.round(x, 3), Math.round(y, 3)]
    },
    CreatePlane () {
      this.CreatePlaneGetStartPoints()
      this.CreatePlaneCreateSvgLayer()
      this.CreatePlaneCreateGreenRect()
      this.CreatePlaneCreatePoints()
      this.PlaneIsShow = true
      this.StartResizeKoef= this.ResizeKoef
    },
    CreatePlaneGetStartPoints () {
      this.sysPlanePoints = [
                          [this.ResizeSysWidth * 0.2, this.ResizeSysHeight * 0.2, 0],
                          [this.ResizeSysWidth * 0.8, this.ResizeSysHeight * 0.2, 1],
                          [this.ResizeSysWidth * 0.8, this.ResizeSysHeight * 0.8, 2],
                          [this.ResizeSysWidth * 0.2, this.ResizeSysHeight * 0.8, 3]
                         ]
      this.sysStartPlanePoints = this.sysPlanePoints.map((el) => {
        return [el[0], el[1]]
      })
    },
    CreatePlaneCreateSvgLayer () {
      let startPoint = this.PointToScale([this.ResizeSysWidth * 0.2, this.ResizeSysHeight * 0.2])
      this.GreenRect = d3.select(".Scene-subcontainer")
                                    .append('svg')
                                    .style("transform-origin",  "0px 0px 0px")
                                    .attr('id', 'SvgGreenRect')
      this.GreenRect.append('g')

      this.SvgPoint = d3.select(".Scene-subcontainer")
                        .append('svg')
                        .attr('id', 'SvgPoints')
      this.SvgPoint.append('g')

    },
    CreatePlaneCreateGreenRect () {
      let GreenRectG = this.GreenRect.select('g')
      GreenRectG.append('polygon')
                    .attr('points', this.ArrayToScale(this.sysStartPlanePoints))
                    .attr('stroke-width', 3)
      this.CreatePlaneChangeGrid()

    },
    CreatePlaneChangeGrid () {
      let newArr = this.ArrayToScale(this.sysStartPlanePoints, false)
      let width = newArr[1][0] - newArr[0][0]
      let height = newArr[2][1] - newArr[1][1]
      let tileWidth = width / this.CreatePlaneTilesCountWidth
      let tileHeight = height / this.CreatePlaneTilesCountHeight
      this.GreenRect.selectAll('line').remove()
      this.GreenRect.select('g').selectAll('.line-x')
        .data(d3.range(0, Math.ceil(this.CreatePlaneTilesCountWidth), 1))
        .enter()
          .append('line')
          .attr('class', "line-x")
          .attr('x1', (d) => d * tileWidth + newArr[0][0])
          .attr('x2', (d) => d * tileWidth + newArr[0][0])
          .attr('y1', newArr[0][1])
          .attr('y2', height + newArr[0][1])
          .style('stroke-width', (d) => {return d%4 == 0 ? 3: 1})
      this.GreenRect.select('g').selectAll('.line-y')
        .data(d3.range(0, Math.ceil(this.CreatePlaneTilesCountHeight), 1))
        .enter()
          .append('line')
          .attr('class', "line-y")
          .attr('y1', (d) => d * tileHeight + newArr[0][1])
          .attr('y2', (d) => d * tileHeight + newArr[0][1])
          .attr('x1', newArr[0][0])
          .attr('x2', width + newArr[0][0])
          .style('stroke-width', (d) => {return d%4 == 0 ? 3: 1})
    },
    // создаем кружочки
    CreatePlaneCreatePoints() {
      let self = this
      this.CreatePlanePointsElems = this.SvgPoint.select('g').selectAll('.PointCirce')
         .data(self.sysPlanePoints)
         .enter()
         .append('circle')
          .attr('class', 'PointCirce')
          .attr('transform', (d) => 'translate(' + self.PointToScale(d[2]) + ')')
          .call(d3.drag()
            .subject((d) => {return {x: self.PointToScale(d[2])[0], y: self.PointToScale(d[2])[1]}})
            .on('drag', function (d) {
              d3.select(this)
                .attr('transform', (d) => 'translate(' + [d3.event.x, d3.event.y] + ')')
              self.sysPlanePoints[d[2]][0]= self.PointOfScale([d3.event.x, d3.event.y])[0]
              self.sysPlanePoints[d[2]][1]= self.PointOfScale([d3.event.x, d3.event.y])[1]
              self.sysPlanePoints = self.sysPlanePoints.slice()
              self.CreatePlaneTransformed()
            }
          ))
    },
    CreatePlaneSetPointParams () {
      this.CreatePlanePointsElems.attr('transform', (d) => 'translate(' + this.PointToScale(d[2]) + ')')
      this.CreatePlaneTransformed()
    },
    CreatePlaneTransformed() {
      let sourcePoints = this.ArrayToScale(this.sysStartPlanePoints, false, this.StartResizeKoef)
      let targetPoints = this.ArrayToScale(this.sysPlanePoints.map((el) => el.slice(0, 2)))
      for (var a = [], b = [], i = 0, n = targetPoints.length; i < n; ++i) {
        let t = targetPoints[i]
        let s = sourcePoints[i]
        a.push([s[0], s[1], 1, 0, 0, 0, -s[0] * t[0], -s[1] * t[0]]), b.push(t[0]);
        a.push([0, 0, 0, s[0], s[1], 1, -s[0] * t[1], -s[1] * t[1]]), b.push(t[1]);
      }
      let X = solve.solve(a, b, true)
      let matrix = [
        X[0], X[3], 0, X[6],
        X[1], X[4], 0, X[7],
           0,    0, 1,    0,
        X[2], X[5], 0,    1
      ].map(function(x) {
        return Math.round(x*1000000)/1000000;
      });
      this.GreenRect.style('transform', "matrix3d(" + matrix + ")");
    }
  },
  mounted () {

    // addEventListener("load", this.CreatePlane)
  }
}
