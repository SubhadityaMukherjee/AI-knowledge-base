---
title: AdaIn

tags: regularize 
date modified: Wednesday, August 10th 2022, 11:41:32 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AdaIn
- [paper](https://arxiv.org/abs/1703.06868v2)
- $$AdaIN(x,y) = \sigma(y) \big( \frac{x-\mu(x)}{\sigma (x)} \big)$$
- Adaptive Instance Normalization is a normalization method that aligns the mean and variance of the content [features](Features.md) with those of the style [features](Features.md).
- no learnable affine [features](Features.md)
- Adaptively computes affine params from style input

