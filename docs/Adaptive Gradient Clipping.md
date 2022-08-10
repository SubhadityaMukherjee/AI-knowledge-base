---
title: Adaptive Gradient Clipping

tags: gradients 
date modified: Wednesday, August 10th 2022, 7:05:42 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Adaptive Gradient Clipping
- clips gradients to the ratio between weight gradient and weight value
- Clipping parameter is more robust than in traditional GC
- Swapping Batch Normalisation for AGC
    - faster training for equally sized models
    - Allows for even larger batch size training

## Backlinks
> - [Gradient Clipping](Gradient Clipping.md)
>   - [[Adaptive Gradient Clipping]]

_Backlinks last generated 2022-08-10 16:56:31_
