---
toc: true
title: AdaIn

categories: ['regularize']
date modified: Monday, October 10th 2022, 2:02:35 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AdaIn
- [paper](https://arxiv.org/abs/1703.06868v2)
- $$AdaIN(x,y) = \sigma(y) \big( \frac{x-\mu(x)}{\sigma (x)} \big)$$
- Adaptive [Instance Normalization](Instance%20Normalization.md.md) is a normalization method that aligns the mean and variance of the content [features](Features.md.md) with those of the style [features](Features.md.md).
- no learnable affine [features](Features.md.md)
- Adaptively computes affine params from style input



