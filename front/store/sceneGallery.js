import axios from 'axios'

export const state = () => ({
  sceneCategoryes: [],
  defaultSceneId: 8
})

export const getters = {
  getSceneCategoryes (state) {
    return state.sceneCategoryes
  },
  getSceneCategoryesNames (state) {
    return state.sceneCategoryes.map((elem) => {return elem.title})
  },
  getDefaultSceneId (state) {
    return state.defaultSceneId
  },
  getСurrentCategoryTitle (state) {
    for (let i of state.sceneCategoryes) {
      if (i.selected == true) {
        return i.title
      }
    }
  }
}
export const actions = {
  getSceneCategoryesFromDb({ commit, state }) {
    const path = `/api/scene/category/get_all_names`
    axios.get(path)
    .then(response => {
      let first = true
      for (let i of response.data) {
        commit('addCategory',{
          'id': i.id,
          'title': i.name,
          'selected': first
        })
        first = false
      }
    })
  }
}
export const mutations = {
    addCategory (state, category) {
      state.sceneCategoryes.push(category)
    },
    changeSelectedSceneCategoryId (state, id) {
      for (let i in state.sceneCategoryes) {
        state.sceneCategoryes[i].selected = false
        if (state.sceneCategoryes[i].id == id) {
          state.sceneCategoryes[i].selected = true
        }
      }
    }
}
