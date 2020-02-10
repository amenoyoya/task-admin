const path = require('path')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  mode: 'development', // 実行モード: development => 開発, production => 本番
  entry: './src/index.js', // エントリーポイント: ソースとなる JS ファイル
  // 出力設定: => ./public/index.js
  output: {
    filename: 'index.js', // バンドル後のファイル名
    path: path.join(__dirname, 'public') // 出力先のパス（※絶対パスで指定すること）
  },
  // モジュール読み込みの設定
  module: {
    rules: [
      // .js ファイルを babel-loader でトランスコンパイル
      {
        test: /\.js$/,
        exclude: /node_modules/, // node_modules/ 内のファイルは除外
        use: [
          // babel-loader を利用
          {
            loader: 'babel-loader',
            options: {
              // @babel/preset-env の構文拡張を有効に
              presets: ['@babel/preset-env']
            }
          }
        ]
      },
      // Vue単一ファイルコンポーネント（.vue ファイル）読み込み設定
      {
        test: /\.vue$/,
        // vue-loaderを使って .vue ファイルをコンパイル
        use: [
          {
            loader: 'vue-loader',
          },
        ],
      },
      // スタイルシート（.css ファイル）読み込み設定
      {
        // .css ファイル: css-loader => vue-style-loader の順に適用
        // - css-loader: cssをJSにトランスコンパイル
        // - style-loader: <link>タグにスタイル展開
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      // Sass（.scss ファイル）コンパイル設定
      {
        // sass-loader => css-loader => vue-style-loader の順に適用
        // vue-style-loader を使うことで .vue ファイル内で <style lang="scss"> を使えるようになる
        test: /\.scss$/,
        use: ['vue-style-loader', 'css-loader', 'sass-loader'],
      },

      /* アイコンローダーの設定 */
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        use: [{
          loader: 'url-loader?mimetype=image/svg+xml'
        }],
      },
      {
        test: /\.(ttf|eot|woff|woff2)(\d+)?(\?v=\d+\.\d+\.\d+)?$/,
        use: [{
          loader: 'url-loader?mimetype=application/font-woff'
        }],
      },
    ]
  },
  // import文で読み込むモジュールの設定
  resolve: {
    extensions: [".js", ".vue"], // .js, .vue をimport可能に
    modules: ["node_modules"], // node_modulesディレクトリからも import できるようにする
    alias: {
      // vue-template-compilerに読ませてコンパイルするために必要な設定
      vue$: 'vue/dist/vue.esm.js',
    },
  },
  // VueLoaderPluginを使う
  plugins: [new VueLoaderPlugin()],
}