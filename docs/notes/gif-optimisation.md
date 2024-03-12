---
title: Optimising GIFs
tags:
  - Images
sources:
  - https://cassidy.codes/blog/2017/04/25/ffmpeg-frames-to-gif-optimization/
  - https://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html
---

Optimising images is a fairly well understood problem, with lots of different solutions and tools. Images can be resized, their pixels grouped, or converted to new, more efficient formats. GIFs however aren't as simple.

Resizing images is fairly simple, and so long as the image isn't too large, not too resource intensive. Resizing GIFs, again, is far more complex.

## 1. Reducing the framerate

Using `ffmpeg`, it's possible to reduce the framerate of a GIF. This script reduces the framerate to 5FPS, which drastically drops the size, as GIFs have poor inter-frame compression.

```bash
#!/usr/bin/env bash

palette="/tmp/palette.png"

filters="fps=5"

ffmpeg -v warning -i $1 -vf "$filters,palettegen=stats_mode=diff" -y $palette

ffmpeg -i $1 -i $palette -lavfi "$filters,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle" -y $2
```

`stats_mode=diff` helps generate a more efficient colour palette, and `diff_mode=rectangle` makes areas which didn't change transparent in the subsequent frames, to further reduce image size.

## 2. Mass optimisation

[`gifsicle`](https://www.lcdf.org/gifsicle/) can optimise and resize a GIF.

It can change the delay between frames, but not strip out frames (thus reducing the FPS), hence the need for `ffmpeg`.

```bash
$ gifsicle -i in.gif -o out.gif --lossy -O3 --resize-width 500
```

This optimises the GIF, without too much emphasis on the resulting quality, and resizes it to 500px wide (maintaining aspect ratio).
