---
title: Gaussian Distortion

tags: augment   
date modified: Wednesday 1st February 2023, Wed
date created: Wednesday 1st February 2023, Wed
---

# Gaussian Distortion
```toc
```

- Grid width and height, and magnitude are kept the same as the random distortion values of 6, 6, and 5, respectively
- The Gaussian distortion has the added parameters of applying the distortion based on the 2D normal distribution
- normal distortion is applied to each grid point on a circular surface (corner="bell") and with default values for the mean and standard deviation ($\mu_{x}$ = $\mu_{y}$ = 0.5,$\sigma_{x}$ = $\sigma_{y}$ = 0.05)
- $$p(x,y) = exp\{-(\frac{(x-\mu_{x})^{2}}{\sigma_{x}} + \frac{(x-\mu_{y})^{2}}{\sigma_{y}}))\}$$

## Backlinks

> - [Comparing Data Augmentation Strategies for Deep Image Classification](Comparing Data Augmentation Strategies for Deep Image Classification.md)
>   - [[Gaussian Distortion]]

_Backlinks last generated 2023-02-01 13:16:25_
