---
title: Bulk rename files
date: 2021-05-14
tags:
  - shell
---

```
rename 's/<in_re>/<out_re>/g' *
```

Useful options:

- `-v`: List files renamed
- `-n`: Dry-run
- `-d`: Act just on the filename
