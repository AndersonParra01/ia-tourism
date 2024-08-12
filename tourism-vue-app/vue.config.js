const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 3000,
    proxy: {
      '/api': {
        target: process.env.API_IA_URL,
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    }
  }
})
