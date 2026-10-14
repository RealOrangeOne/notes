---
title: Stop saving bash history
tags:
  - Shell
---

## Disable history for a given session

```shell
$ unset HISTFILE
```

or:

```shell
$ set +o history
```

## Clear history

```shell
$ history -c
```
