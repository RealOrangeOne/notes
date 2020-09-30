module.exports = {
  siteMetadata: {
    title: 'notes',
    description: 'A description',
    author: 'TheOrangeOne',
    siteUrl: 'https://notes.theorangeone.net'
  },
  plugins: [
    {
      resolve: 'gatsby-theme-code-notes',
      options: {
        contentPath: 'notes',
        basePath: '/',
        showThemeInfo: false,
        showDescriptionInSidebar: true,
      },
    },
    'gatsby-plugin-robots-txt',
    'gatsby-plugin-sitemap'
  ],
}
