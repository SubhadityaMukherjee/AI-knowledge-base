---
title: Mixup
tags: regularize 
---

# Mixup
- Randomly sample two examples $(x_{i}, y_{i})$ and $(x_{j}, y_{j})$
- New example by weighted [[1D piecewise linear interpolation]]
- $$\hat x = \lambda x_{i}+(1-\lambda)x_{j}$$
- $$\hat y = \lambda y_{i}+(1-\lambda)y_{j}$$
- $\lambda \in [[Beta Distribution|0,1]]
- New example $(\hat x, \hat y)$


































































































## Backlinks

> - [Augmentation](Augmentation.md)
>   - [[Mixup]]

_Backlinks last generated 2022-07-26 20:33:15_
