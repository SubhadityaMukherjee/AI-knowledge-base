---
title: Lp Regularization
---

# Lp [[Regularization]]
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
		- ![[Pasted image 20220306133032.png]]
- Tune $$\lambda$$
	- Grid search : log scale
	- Too large : underfit, too small : overfit
	- [[Cross validation]] required




