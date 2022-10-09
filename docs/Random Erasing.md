---
title: Random Erasing
tags: augment
---

# Random Erasing
- deletes contiguous rectangular image regions similar to cutout with minor differences in region selection procedure.
- Opposite to cutout, where deletion is applied on all the images, here it is performed with a probability of either applying it or not
- In every iteration, region size is defined randomly with upper and lower limits on region area and aspect ratio.
- Additional to this, random erasing provides region-aware deletion for object detection and person identification tasks
- Regions inside the object bounding boxes are randomly erased to generate occlusions

## Backlinks

> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[Random Erasing]]

_Backlinks last generated 2022-10-09 12:22:37_
