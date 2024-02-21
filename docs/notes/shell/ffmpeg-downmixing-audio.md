---
title: Downmixing audio channels
tags:
  - Media
sources:
  - https://trac.ffmpeg.org/wiki/AudioChannelManipulation
---

```bash
ls -1 *.mp4 | xargs -I{} ffmpeg -y -i {} -ac 2 -c:v copy /path/to/out/{}
```

Downmixes multi-channel audio into stereo. Reduces the chances of weird things happening during playback.

`-c:v copy` is important for performance as it means the video isn't re-encoded (10x improvement in speed).
