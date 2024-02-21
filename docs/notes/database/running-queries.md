---
title: Monitor running queries
tags:
  - PostgreSQL
sources:
  - https://techmango.org/2017/11/04/monitor-running-queries-postgresql/
---

View a list of running queries:

```sql
SELECT
  datname,
  pid,
  usename,
  client_addr,
  client_port,
  xact_start,
  backend_start,
  query_start,
  state,
  query
FROM pg_stat_activity
ORDER BY query_start ASC
```

View list of non-idle connections:

```sql
SELECT
  datname,
  pid,
  usename,
  client_addr,
  client_port,
  xact_start,
  backend_start,
  query_start
FROM pg_stat_activity
WHERE
  state != 'idle'
ORDER BY query_start ASC
```
