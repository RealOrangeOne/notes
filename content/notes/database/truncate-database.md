---
title: Truncate a database from the inside
date: 2020-10-07
tags:
  - PostgreSQL
---

How to delete database from the inside, with only access to that database.

The primary way this works is by using `pg_dump`'s ability to drop a schema before recreating it.

This creates a dump of the database without any data, and with a fresh schema (drop then rebuild). This output is then `grep`'d to only contain the drops.

```shell-session
$ pg_dump -cs "postgres://<database url>" | grep DROP > drops.psql.sql
```

Now run the drops. These drops are specifically designed for this schema so should be complete and in the correct order.

```shell-session
$ psql "postgres://<database url>" < drops.psql.sql
```
