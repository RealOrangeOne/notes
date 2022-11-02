---
title: Stop saving bash history
emoji: 🤔
tags:
  - Shell
modified: 2022-11-02
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
