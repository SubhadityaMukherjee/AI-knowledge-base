---
title: Sparse Dict Learning Loss
tags: loss 
date modified: Wednesday, August 10th 2022, 7:05:46 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sparse Dict Learning [Loss](loss.md)
- $$L(X) = n^{-1}\Sigma_i^n ||x_i - Dr_i ||^2 + \lambda \Sigma_i |r_i|$
- $\lambda \Sigma_i |r_i|$ is Lasso/L1 [Lp Regularization](Lp%20Regularization.md)
- Predictions :  $r = argmin_r ||x- Dr_i ||^2 + \lambda \Sigma_i |r_i|$

