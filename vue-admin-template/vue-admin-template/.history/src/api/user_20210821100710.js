import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login/',
    method: 'post',
    data
  })
}

export function register(data) {
  return request({
    url: '/users/users',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/users/getinfo/',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}
