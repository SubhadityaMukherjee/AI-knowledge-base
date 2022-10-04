---
title: Sparse Dict Learning Loss
tags: loss 
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sparse Dict Learning [[loss|Loss]]
- $$L(X) = n^{-1}\Sigma_i^n ||x_i - Dr_i ||^2 + \lambda \Sigma_i |r_i|$
- $\lambda \Sigma_i |r_i|$ is Lasso/L1 [[Lp Regularization]]
- Predictions :  $r = argmin_r ||x- Dr_i ||^2 + \lambda \Sigma_i |r_i|$

## Backlinks

> - [Dictionary Learning](Dictionary Learning.md)
>   - [[Sparse Dictionary Learning Loss]]

_Backlinks last generated 2022-10-04 13:01:19_
