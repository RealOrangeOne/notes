---
title: Scaling Heroku's release type
tags:
  - Heroku
---

During `release`, it's possible to consume so much memory, Heroku kills the dyno before it finishes executing.

```
heroku[release.xxxx]: Process running mem=1038M(202.8%)
heroku[release.xxxx]: Error R15 (Memory quota vastly exceeded)
heroku[release.xxxx]: Stopping process with SIGKILL
heroku[release.xxxx]: Process exited with status 137
heroku[release.xxxx]: State changed from up to complete
```

When that happens, the release fails (even though it may say "complete"). Whilst it's a good idea not to use huge amounts of memory during release, sometimes it's unavoidable.

Releases run in a `Standard-1X` dyno, regardless of what the other dynos are set to. This has a 512MB RAM limit, however Heroku will let it push over for short periods.

Setting the `release` dyno type can't be done from the dashboard, but can be done from the CLI:

```
heroku ps:type release=Standard-1X -a <app>
```

!!! warning
    When running `Eco` or `Basic` dynos, the release container is configured to match. It's not possible to use other types of dyno on these plans.
