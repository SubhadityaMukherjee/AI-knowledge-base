---
title: GridMask
tags: augment
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# GridMask
- The algorithm tries to overcome drawbacks of Cutout, Random Erasing, and Hide and Seek that are prone to deleting important information entirely or leaving it untouched without making it harder for the algorithm to learn.
- To handle this, GridMask creates multiple blacked-out regions in evenly spaced grids to maintain a good balance between deletion and retention of critical information
- The number of masking grids and their sizes are tuneable

## Backlinks
> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[GridMask]]

_Backlinks last generated 2022-10-09 12:22:37_
