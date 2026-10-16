---
title: Colophon
---

This site is built using [Hugo](https://gohugo.io) and the [Notebook](https://github.com/its-ammu/hugo-notebook) theme. I've made quite a few modifications to the theme, notably (but not limited to):

- The tag list on the homepage
- Search (see below)
- Sources on notes which include details from elsewhere
- Admonitions. Like this:

{{% admonition danger %}}
High voltage!
{{% /admonition%}}

## Hosting

The code is hosted on [GitHub](https://github.com/RealOrangeOne/notes/), and deployed to GitHub Pages.

For now...

## Search

Despite this being {{< now "2006" >}}, Hugo _still_ doesn't have a built-in search story. Instead deferring it to the user to both build build a content index and search through it on the client.

A long time ago, when my website was built on Hugo, [I did exactly that](https://theorangeone.net/posts/hugo-website-search/). It worked, but it wasn't exactly elegant.

The search for this site is different. It uses [pagefind](https://pagefind.app/), which handles building the index and all the frontend needed to do it. A few HTML components, and a command-line tool run after the Hugo build is all it needs. Search is fast, efficient, and most importantly not my problem! 

Just press `/` or click the widget in the sidebar and off you go.

## History

It's been through a few iterations in the past, starting with [`gatsby-theme-code-notes`](https://github.com/mrmartineau/gatsby-theme-code-notes/), on to [`hugo-theme-notes`](https://github.com/RealOrangeOne/hugo-theme-notes/), followed by a pretty cursed [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) setup, and finally here.

I really need to stop treating my notes site like a project.
