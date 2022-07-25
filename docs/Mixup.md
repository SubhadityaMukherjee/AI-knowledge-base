---
title: Mixup
tags: regularize 
---

# Mixup
- Randomly sample two examples $(x_{i}, y_{i})$ and $(x_{j}, y_{j})$
- New example by weighted [1D piecewise linear interpolation](1D%20piecewise%20linear%20interpolation.md)
- $$\hat x = \lambda x_{i}+(1-\lambda)x_{j}$$
- $$\hat y = \lambda y_{i}+(1-\lambda)y_{j}$$
- $\lambda \in [0,1]$  is a random number from [Beta Distribution](Beta%20Distribution.md)
- New example $(\hat x, \hat y)$






























































































