---
title: Fixing author date and signature when rebasing git commits
tags:
  - Git
sources:
  - https://til.simonwillison.net/git/git-filter-repo
  - https://stackoverflow.com/a/73314321
---

When rebasing commits, it's common that the author date gets reset (since you're re-authoring the commit).

Simon Willison's [solution](https://til.simonwillison.net/git/git-filter-repo) using `git-filter-repo` works, but strips GPG signatures.

To restore the GPG signature, first run the `git-filter-repo` trick, then run:

```shell-session
$ git \
  -c rebase.instructionFormat='%s%nexec GIT_COMMITTER_DATE="%cD" GIT_AUTHOR_DATE="%aD" git commit --amend --no-edit -S' \
  rebase -f <commit>
```

I'm sure there's a way to combine the 2.
