---
title: Mixup
---

# Mixup
- Randomly sample two examples $(x_{i}, y_{i})$ and $(x_{j}, y_{j})$
- New example by weighted [[1D piecewise linear interpolation]]
- $$\hat x = \lambda x_{i}+(1-\lambda)x_{j}$$
- $$\hat y = \lambda y_{i}+(1-\lambda)y_{j}$$
- $\lambda \in [0,1]$  is a random number from [[Beta Distribution]]
- New example $(\hat x, \hat y)$








