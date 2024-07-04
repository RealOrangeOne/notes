---
title: Infinite-expiry access tokens on self-hosted GitLab
tags:
  - GitLab
---

The ability to create personal access tokens without expiry was [deprecated](https://gitlab.com/gitlab-org/gitlab/-/issues/369122) in GitLab 15.4 and [removed](https://gitlab.com/gitlab-org/gitlab/-/issues/392855) in GitLab 16.0. For security reasons, expiring tokens makes sense. However, in many cases I'd much rather set them infinite so I can easily put them in version control and not worry about them expiring. If an attacker can access the token, I've already got bigger problems.

!!! warning
    This solution **only** works on self-hosted GitLab. It will not work with [gitlab.com](https://gitlab.com)!

This requires connecting to the database. Exactly how to do that will vary based on your deployment (it's probably `gitlab-psql`).

## 1. Find the token:

```psql
gitlabhq_production=> select * from personal_access_tokens order by created_at desc limit 1;
```

Assuming you just made the token, it should be the latest. If it's not, you'll need to tweak the query.

## 2. Find the id, and confirm it's the right one:

```psql
gitlabhq_production=> select * from personal_access_tokens where id=<id>;
```

You don't want to change the wrong one!

## 3. Increase the date

```psql
update personal_access_tokens set expires_at=expires_at + interval '100 years' where id=<id>;
```

In 100 years, it's someone else's problem.
