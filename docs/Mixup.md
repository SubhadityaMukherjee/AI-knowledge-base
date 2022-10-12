---
title: Mixup
tags: regularize 
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Mixup
- Randomly sample two examples $(x_{i}, y_{i})$ and $(x_{j}, y_{j})$
- New example by weighted [[1D piecewise linear interpolation]]
- $$\hat x = \lambda x_{i}+(1-\lambda)x_{j}$$
- $$\hat y = \lambda y_{i}+(1-\lambda)y_{j}$$
- $\lambda \in [[Beta Distribution|0,1]]
- New example $(\hat x, \hat y)$

