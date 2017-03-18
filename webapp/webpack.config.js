const path = require('path');

const ExtractTextPlugin = require("extract-text-webpack-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');

const extractSass = new ExtractTextPlugin({
  filename: "[name].css",
  disable: process.env.BUILD_ENV !== "production"
});

module.exports = {
  entry: './src/index.js',

  output: {
    path: path.join(__dirname, "dist"),
    filename: 'index.js'
  },

  resolve: {
    extensions: ['.js', '.elm']
  },

  module: {
    rules: [
      {
        test: /\.png$/,
        use: 'file-loader?name=img/[name].[ext]'
      },
      {
        test: /\.css$/,
        use: 'file-loader?name=[name].[ext]'
      },
      {
        test: /\.elm$/,
        exclude: [/elm-stuff/, /node_modules/],
        use: [
          'elm-hot-loader',
          'elm-webpack-loader'
        ]
      },
      {
        test: /\.scss$/,
        use: extractSass.extract({
          use: [{
            loader: "css-loader"
          }, {
            loader: "sass-loader"
          }],
          // use style-loader in development
          fallback: "style-loader"
        })
      }
    ],

    noParse: /\.elm$/
  },

  plugins: [
    extractSass,
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.html'
    })
  ],

  devServer: {
    inline: true,
    stats: 'errors-only'
  }
};
