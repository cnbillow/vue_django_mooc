import Home from '../views/Home/Home'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/search_result/:searchKey',
    name: 'search_result',
    component: () => import('../views/SearchResult/SearchResult'),
    props: { default: true, sidebar: false }
  }
]

export default routes
