export default {
  plugins: [
    {
      src: '~/plugins/numeric-solve.js',
      ssr: false
    },
    {
      src: '~/plugins/global.js'
    }],
  env: {
    baseUrl: process.env.BASE_URL || 'http://localhost:3000',
    reqUrl: 'http://127.0.0.1:3000/api/'
  },
  modules: [
    '@nuxtjs/axios'
  ],
  axios: {
    proxy: true
  },
  proxy: {
    '/api/': { target: 'http://127.0.0.1:5000/', pathRewrite: {'^/api/': ''} , secure: false, changeOrigin: true}
  },
}
