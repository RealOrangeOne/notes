module.exports = {
  siteMetadata: {
    title: 'Notes',
    description: 'Notes and snippets and things',
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
    'gatsby-plugin-sitemap',
    'gatsby-plugin-sri',
    {
      resolve: 'gatsby-plugin-plausible',
      options: {
        domain: 'notes.theorangeone.net',
        customDomain: 'plausible.theorangeone.net'
      }
    }
  ],
}
