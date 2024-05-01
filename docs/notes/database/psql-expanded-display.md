---
title: View wide tables with psql
tags:
  - PostgreSQL
sources:
  - https://stackoverflow.com/a/26040852
---

When making a query with lots of columns, it can become so wide that it wraps, making the results incredibly difficult to read.

To combat this, you can toggle "Expanded display" using `\x`:

```psql
website=# \x
Expanded display is on.
website=# \x
Expanded display is off.
```

Expanded display changes the output from a conventional table to a key/value mapping:

```psql
website=# select * from wagtailcore_page order by title limit 1;
-[ RECORD 1 ]--------------+---------------------------------------
id                         | 207
path                       | 0001000100020034
depth                      | 4
numchild                   | 0
title                      | Adding blog posts to my GitHub profile
slug                       | github-readme-blog-posts
live                       | t
has_unpublished_changes    | f
url_path                   | /home/posts/github-readme-blog-posts/
seo_title                  |
show_in_menus              | t
search_description         |
go_live_at                 |
expire_at                  |
expired                    | f
content_type_id            | 14
owner_id                   | 1
locked                     | f
latest_revision_created_at | 2024-02-18 21:39:50.893249+00
first_published_at         | 2024-02-06 20:55:01.699808+00
live_revision_id           | 574
last_published_at          | 2024-02-18 21:39:50.999476+00
draft_title                | Adding blog posts to my GitHub profile
locked_at                  |
locked_by_id               |
translation_key            | 3714dd50-fabe-4d56-b4bd-fdabc27568a4
locale_id                  | 1
alias_of_id                |
latest_revision_id         | 574
```
