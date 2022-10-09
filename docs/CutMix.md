---
title: CutMix
tags: augment
---

# CutMix
- images are augmented by sampling patch coordinates, x, y, h, w from a uniform distribution
- selected patch is replaced at the
- corresponding location with a patch from the other randomly picked image from the current mini-batch during training.
- M is the image mask, xa and xb are images, λ is the proportion of label, and ya and yb are the labels of images.
- $$x_{new}= M.x_{a}+(1-M).x_{b}$$
- $$y_{new}= \lambda.y_{a}+ (1-\lambda).y_{b}$$

