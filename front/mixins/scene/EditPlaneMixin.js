export default {
  methods: {
    EditPlane (val, key) {
      this.CreatePlane()
      this.sysPlanePoints = val.imagePoints
      this.isEdit = true
      this.EditKey = key
      this.CreatePlaneSetPointParams()
      this.CreatePlaneTransformed()
    }
  }
}
