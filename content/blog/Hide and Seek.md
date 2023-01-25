---
title: Hide and Seek
tags: augment
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Hide and Seek
- divides an image into a specified number of grids and turns on and off each grid with an assigned probability
- various image regions are deleted, and they can be connected or disconnected from each other
- Values in turned-off regions are replaced with the average of all the pixel values in the entire dataset.

## Backlinks

> - [GridMask](GridMask.md)
>   - The algorithm tries to overcome drawbacks of [[Cutout]], [[Random Erasing]], and [[Hide and Seek]] that are prone to deleting important information entirely or leaving it untouched without making it harder for the algorithm to learn.

_Backlinks last generated 2023-01-25 01:31:24_
