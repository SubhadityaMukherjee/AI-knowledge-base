---
title: Lp Regularization
tags: regularize
date modified: Thursday, August 11th 2022, 12:32:51 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Lp [Regularization](Regularization.md)
- ![[assets/Pasted image 20220626150853.png](from%20%5Blink))
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
		- Encourages optimization trajectory perpendicular to isocurves
		- ![im](assets/Pasted%20image%2020220306133032.png)
- Tune $$\lambda$$
	- Grid search : log scale
	- Too large : underfit, too small : overfit
	- [Cross Validation](Cross%20Validation.md) required

