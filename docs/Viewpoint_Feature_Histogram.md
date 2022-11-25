---
title: Viewpoint Feature Histogram
tags: robotics 
---
```toc
```
# Viewpoint Feature Histogram
- VFH produces a histogram that encodes the geometry of the object and its viewpoint.
- For every pair of a point and the center of mass, a reference frame is constructed and the three angular variations are computed (a, q, f) and also d which represents distance between (point, center of mass)
- Another statistical feature is computed between the central viewpoint direction and the normal estimated at each point.
- The quality of VFH description depends on the quality of the surface normal estimation at each point.
- ![[images/Pasted image 20221103123406.png]]

## Backlinks

> - [](journals/2022-11-03.md)
>   - [[Viewpoint_Feature_Histogram]]

_Backlinks last generated 2022-11-25 12:02:50_
