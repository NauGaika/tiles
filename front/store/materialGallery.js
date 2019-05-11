import axios from 'axios'
export const state = () => ({
  materialCategoryes: [],
  defaultMaterialId: 21
})

export const getters = {
  getMaterialCategoryes (state) {
    return state.materialCategoryes
  },
  getMaterialCategoryNames (state) {
    return state.materialCategoryes.map((elem) => {return elem.title})
  },
  getMaterialCategoryId (state) {
    return (title) => {
      let resTitle = ''
      for (let i of state.materialCategoryes) {
        if (i.title == title) {
          resTitle = i.title
          break
        }
      }
      return resTitle
    }
  },
  getСurrentCategoryTitle (state) {
    for (let i of state.materialCategoryes) {
      if (i.selected == true) {
        return i.title
      }
    }
  }
}

export const actions = {
  getMaterialCategoryesFromDb({ commit, state }) {
    const path = `/api/material/category/get_all_names`
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
    state.materialCategoryes.push(category)
  },
    changeMaterialCategoryId (state, id) {
      for (let i in state.materialCategoryes) {
        state.materialCategoryes[i].selected = false
        if (state.materialCategoryes[i].id == id) {
          state.materialCategoryes[i].selected = true
        }
      }
    }
}
