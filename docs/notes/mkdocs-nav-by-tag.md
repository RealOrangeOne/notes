---
title: Navigate mkdocs by tag
tags:
  - mkdocs
---

The sidebar for this notes site uses tags for the hierarchy, rather than by the filesystem structure.

This works by retrieving the tags for each note, creating fake sections for each, and replacing the existing sections with those.

!!! warning
    Here be dragons.

```python
{! ../hooks/tag_nav.py !}
```
