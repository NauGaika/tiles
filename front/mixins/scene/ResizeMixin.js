export default {
  data () {
    return {
      ResizeSysWidth: 1,
      ResizeSysHeight: 1,
      ResizeCurrentWidth: 1,
      ResizeImgSrc: "",
    }
  },
  props: {
    img: {
      default: '/img/scene/scene_8/scene.png',
    },
    scale: {
      default: 1
    }
  },
  computed: {
    width () {
      return Math.round(this.ResizeSysWidth * this.ResizeKoef, 3)
    },
    height () {
      return Math.round(this.ResizeSysHeight * this.ResizeKoef, 3)
    },
    ResizeKoef () {
      return this.ResizeCurrentWidth / this.ResizeSysWidth
    }
  },
  watch: {
    img (file) {
      let reader = new FileReader()
      reader.onloadend = () => {
        this.ResizeImgSrc = reader.result
        this.ResizeGetImageDimensions()
      }
      if (typeof(this.img) == 'object') {
        reader.readAsDataURL(this.img)
      }
      if (typeof(this.img) == 'string') {
        this.ResizeImgSrc = this.img
        this.ResizeGetImageDimensions()
      }
    },
    scale (res) {
      this.ResizeSetBackgroundSize()
    }
  },
  methods: {
    getImgSrc () {
      if (typeof this.img == 'string') {
        this.ResizeImgSrc = this.img
      }
      if (process.client) {
        let reader = new FileReader()
        reader.onloadend = () => {
          reader.result
        }
        if (typeof(this.img) == 'object') {
          reader.readAsDataURL(this.img)
        }
      }
    },
    ResizeChange() {
      this.ResizeIs = !this.ResizeIs
    },
    ResizeGetImageDimensions () {
      let image = new Image()
      let src = this.ResizeImgSrc
      image.src = src
      image.onload = () => {
        this.ResizeSysWidth = image.width
        this.ResizeSysHeight = image.height
      }
    },
    ResizeSetCurrentWidth () {
      this.ResizeCurrentWidth = this.$refs.divElem.clientWidth
      this.ResizeSetBackgroundSize()
    },
    ResizeSetBackgroundSize () {
      this.$refs.imgElem.style['background-size'] = this.width / this.scale + 'px'
    }
  },
  mounted () {
    this.ResizeImgSrc = this.img
    if (process.client) {
      window.addEventListener('resize', this.ResizeSetCurrentWidth)
      window.addEventListener('load', this.ResizeSetCurrentWidth)
      window.addEventListener('load', this.ResizeGetImageDimensions)
      window.addEventListener('load', this.ResizeSetBackgroundSize)
    }
  },
  updated () {

  },
  beforeDestroy () {
    if (process.client) {
      window.removeEventListener('resize', this.ResizeSetCurrentWidth)
    }
  }
}
