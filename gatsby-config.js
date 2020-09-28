module.exports = {
  siteMetadata: {
    title: 'notes',
    description: 'A description',
    author: 'TheOrangeOne',
  },
  plugins: [
    {
      resolve: 'gatsby-theme-code-notes',
      options: {
        contentPath: 'notes',
        basePath: '/',
        showThemeInfo: true,
        showDescriptionInSidebar: true,
      },
    },
  ],
}
