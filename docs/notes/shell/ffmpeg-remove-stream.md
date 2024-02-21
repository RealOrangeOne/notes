---
title: Strip audio / subtitle stream with ffmpeg
tags:
  - Media
sources:
  - https://stackoverflow.com/a/38162168
---

```bash
ls -1 *.mp4 | xargs -I{} ffmpeg -y -i {} -map 0 -map -0:a:0 -c copy /path/to/out/{}
```

`-map -0:a:0` removes the 0th audio stream.

- v - video, such as `-map -0:v`
- a - audio, such as `-map -0:a`
- s - subtitles, such as `-map -0:s`
- d - data, such as `-map -0:d`
