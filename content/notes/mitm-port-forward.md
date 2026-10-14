---
title: Simple reverse proxy
tags:
  - Networking
---

This uses [`mitmproxy`](https://docs.mitmproxy.org/stable), which can proxy both HTTP and HTTPS.

```
mitmproxy --mode reverse:http://localhost:8000
```
