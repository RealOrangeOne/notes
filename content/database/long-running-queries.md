---
title: Find and kill long running queries
tags:
  - PostgreSQL
link: https://medium.com/little-programming-joys/finding-and-killing-long-running-queries-on-postgres-7c4f0449e86d
---

# Running queries

View a list of queries running longer than 5 minutes:

```sql
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

Also see [running queries](../running-queries).

# Stopping a given connection

```sql
SELECT pg_cancel_backend(pid);
```

`pid` being the relevant value from `pg_stat_activity.pid`.

# Killing a given connection

```sql
SELECT pg_terminate_backend(pid);
```

Should be avoided, as it's synonymous with `kill -9`.
