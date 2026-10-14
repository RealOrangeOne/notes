---
title: Finding large Prometheus Series
tags:
  - Prometheus
---

When looking through a sea of stats, it's hard to find which metrics are consuming the most data (especially when billed by series).

With a list of metrics, you can start looking at sensible prefixes, such as by exporter. Per exporter, it gets more complex.

It's fairly easy to list all metrics, and count them:

```
count({__name__=~".+"})
```

This query narrows down series based on the first letter after the exporter prefix (eg `node_`):

```
count by (prefix) (label_replace({__name__=~".+"}, "prefix", "$1 $2", "__name__", "(.+?)_(.{1}).+"))
```

Returned metrics will contain a "prefix" label with the exporter prefix and first letter of the rest of the metric name. Tweak `{1}` in the final `label_prefix` argument to extend how many letters are considered.
