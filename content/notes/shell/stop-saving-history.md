---
title: Stop saving bash history
date: 2022-11-02
tags:
  - shell
---

```shell-session
$ unset HISTFILE
```

or:

```shell-session
$ set +o history
```

## Clear history

```shell-session
$ history -c
```
