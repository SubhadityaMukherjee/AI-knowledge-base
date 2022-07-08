---
title: Lp Regularization
tags: regularize
---

# Lp [[Regularization]]
- ![](assets/Pasted%20image%2020220626150853.png) (from [link](https://github.com/christianversloot/machine-learning-articles/blob/main/which-regularizer-do-i-need-for-training-my-neural-network.md))
- Tikhonov
- Penalty considering weights
- $$L^\ast(\theta) = L(\theta) + \lambda \Sigma_i |\theta_i|^p$$
	- Lasso
		- p = 1
		- Sparse
		- With linear model : feature selection
	- Weight Decay
		- p = 2
		- [[Bayesian]]
		- Encourages optimization trajectory perpendicular to isocurves
		- ![im](assets/Pasted%20Image%2020220306133032.png)
- Tune $$\lambda$$
	- Grid search : log scale
	- Too large : underfit, too small : overfit
	- [[Cross validation]] required














