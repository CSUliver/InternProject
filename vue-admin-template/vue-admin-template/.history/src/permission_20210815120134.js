import router from './router'
import store from './store'
import { Message } from 'element-ui'
import NProgress from 'nprogress' 
import 'nprogress/nprogress.css'
import { getToken } from '@/utils/auth' 
import getPageTitle from '@/utils/get-page-title'

NProgress.configure({ showSpinner: false })

const whiteList = ['/login'] 

router.beforeEach(async(to, from, next) => {
  NProgress.start()

  document.title = getPageTitle(to.meta.title)
  const hasToken = getToken()

  if (hasToken) {
    if (to.path === '/login') {
      next({ path: '/' })
      NProgress.done()
    } else {
      
      const hasRoles = store.getters.roles && store.getters.roles.length > 0
      if (hasRoles) {
        next()
      } else {
        try {
          // 获取roles
          //const { roles } = await store.dispatch('user/getInfo')
          
          const { results } = await store.dispatch('user/getInfo')
          console.log(results,'permission...')
          
          let roles = []
          results[0].groups.forEach(item=>{
              roles.push(item.name)
          })
          console.log(roles,'per roles...')
          // 获取通过权限的路由
          const accessRoutes = await store.dispatch('permission/generateRoutes', roles)
          // 更新路由
          router.options.routes = store.getters.permission_routes

          router.addRoutes(accessRoutes)

          next({ ...to, replace: true })
        } catch (error) {
          await store.dispatch('user/resetToken')
          Message.error(error || 'Has Error')
          next(`/login?redirect=${to.path}`)
          NProgress.done()
        }
      }
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      next(`/login?redirect=${to.path}`)
      NProgress.done()
    }
  }
})

router.afterEach(() => {
  NProgress.done()
})
