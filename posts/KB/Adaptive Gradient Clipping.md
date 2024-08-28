---
toc: true
title: Adaptive Gradient Clipping

tags: ['gradients']
date modified: Monday, October 10th 2022, 2:02:35 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Adaptive [[Gradient Clipping.md|Gradient Clipping]]
- clips gradients to the ratio between weight gradient and weight value
- Clipping parameter is more robust than in traditional GC
- Swapping Batch Normalisation for AGC
    - faster training for equally sized models
    - Allows for even larger batch size training



