import { asyncRoutes, constantRoutes } from '@/router'


/**
 * Use meta.role to determine if the current user has permission
 * @param roles
 * @param route
 */
function hasPermission(roles, route) {
  if (route.meta && route.meta.roles) {
    return roles.some(role => route.meta.roles.includes(role))
  } else {
    return true
  }
}

/**
 * Filter asynchronous routing tables by recursion
 * @param routes asyncRoutes
 * @param roles
 */
export function filterAsyncRoutes(routes, roles) {
  const res = []

  routes.forEach(route => {
    const tmp = { ...route }
    if (hasPermission(roles, tmp)) {
      if (tmp.children) {
        tmp.children = filterAsyncRoutes(tmp.children, roles)
      }
      res.push(tmp)
    }
  })

  return res
}

const state = {
  routes: [],
  addRoutes: []
}

const mutations = {
  SET_ROUTES: (state, routes) => {
    
    state.routes = constantRoutes.concat(routes)
  }
}


const actions = {
  generateRoutes({ commit }, roles) {
    return new Promise(resolve => {
      // 定义一个变量，用来存放可以访问的路由表
      let accessedRoutes
      // 判断当前用户是否包含admin
      if (roles.includes('admin')) {
        // 如果包含就可以访问所有路由
        // 实现动态路由的思路关键点在这里，将ansyncRoutes改造成从数据库中获取
        accessedRoutes = asyncRoutes || []
      } else {
        // 否则根据角色过滤掉不能访问的路由表
        accessedRoutes = filterAsyncRoutes(asyncRoutes, roles)
      }
      // commit
      commit('SET_ROUTES', accessedRoutes)
      // 返回
      resolve(accessedRoutes)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}