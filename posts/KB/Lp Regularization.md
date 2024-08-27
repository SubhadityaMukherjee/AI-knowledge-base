---
toc: true
title: Lp Regularization
categories: ['regularize']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Lp [Regularization](Regularization.md)
- ![im](images/Pasted%image%20220626150853.png)
- Tikhonov
- Penalty considering weights
- $$L^\ast(\theta) = L(\theta) + \lambda \Sigma_i |\theta_i|^p$$
	- Lasso
		- p = 1
		- Sparse
		- With linear model : feature selection
	- Weight Decay
		- p = 2
		- [Bayesian](Bayesian.md)
		- Encourages optimization [trajectory](Trajectory.md) perpendicular to isocurves
		- ![im](Pasted%20image%2020220306133032.png)
- Tune $$\lambda$$
	- Grid search : log scale
	- Too large : underfit, too small : overfit
	- [Cross Validation](Cross%20Validation.md) required



