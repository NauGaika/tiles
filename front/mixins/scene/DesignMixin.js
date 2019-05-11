import * as d3 from "d3"

export default {
  methods: {
    DesignShowImg (img) {
      let isFirst = d3.select('.Scene-subcontainer').selectAll('.DesignShowNewImg').size() == 0
      if (isFirst) {
        console.log(isFirst)
        let el = d3.select('.Scene-subcontainer').append('img').style('opacity', 0).attr('src', img).attr('class', 'DesignShowNewImg')
        el.transition().style('opacity', 1).duration(500)
      } else {
        let privious = d3.select('.Scene-subcontainer').select('.DesignShowNewImg')
        let el = d3.select('.Scene-subcontainer').append('img').style('opacity', 0).attr('src', img).attr('class', 'DesignShowNewImg')
        el.transition().style('opacity', 1).duration(500)
        setTimeout(() => {
          privious.remove()
        }, 1000)
      }
    }
  }
}
