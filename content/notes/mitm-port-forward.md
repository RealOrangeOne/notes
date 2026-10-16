---
title: Simple reverse proxy
date: 2021-05-14
tags:
  - networking
---

This uses [`mitmproxy`](https://docs.mitmproxy.org/stable), which can proxy both HTTP and HTTPS.

```shell-session
$ mitmproxy --mode reverse:http://localhost:8000
```
