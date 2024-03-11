---
title: Scheduler-only Heroku apps
tags:
  - Heroku
---

If everything you run is already in Heroku, it can be useful to run even simple scheduled tasks there too, to save integrating and running services on another hosting provider.

Heroku's scheduler only has a few intervals (every 10 minutes, hourly at X, daily at X), but if these work for you (or you can make use of them), then it's very cost-effective and simple.

Whilst Heroku is clearly designed for web apps, there's no reason you _need_ a `web` dyno. So long as there's something Heroku _could_ run, you can scale the `web` dyno to 0 and it'll never get run. [`sleep infinity`](https://theorangeone.net/posts/efficient-sleeping/) is a good command to use as a placeholder. For common-runtime apps, add this to the `Procfile`. For docker-based apps, set it as the `CMD`.

Then, deploy your codebase (which might just be a collection of `bash` scripts), add Heroku's [Scheduler](https://elements.heroku.com/addons/scheduler), and use it like you normally would. Heroku only charges for the scheduler based on the dynos it runs (rather than a flat fee for using it), so a job which only runs for an hour a month costs just ~$0.010.

It's recommended to turn on [Maintenance Mode](https://devcenter.heroku.com/articles/maintenance-mode) for the app, just in case something does discover the URL, as it results in a nicer error (for you and them).
