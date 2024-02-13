---
title: Rebase commits done on the wrong branch
tags:
  - Git
link: https://git-scm.com/book/en/v2/Git-Branching-Rebasing#_more_interesting_rebases
---

```sh
git rebase --onto master server client
```

> Take the `client` branch, figure out the patches since it diverged from the `server` branch, and replay these patches in the client branch as if it was based directly off the `master` branch instead.
