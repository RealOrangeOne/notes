---
title: Hide short Table of Contents
tags:
  - Mkdocs
---

Some of my notes don't have headings. Others have barely any. However, the Table of Contents area takes up a large area of screen for no reason.

This hook only shows the Table of Contents area when there are more than 4 headings (at any level).

```python
{! ../hooks/hide_toc.py !}
```
