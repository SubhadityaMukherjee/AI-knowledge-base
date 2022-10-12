---
title: Lp Regularization
tags: regularize
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Lp [[Regularization]]
- ![[from [link|[assets/Pasted image 20220626150853.png]])
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
		- Encourages optimization [[Trajectory|trajectory]] perpendicular to isocurves
		- ![[assets/Pasted image 20220306133032.png|im]]
- Tune $$\lambda$$
	- Grid search : log scale
	- Too large : underfit, too small : overfit
	- [[Cross Validation]] required

## Backlinks
> - [Regularization](Regularization.md)
>   - [[Lp Regularization]]
>
> - [Sentiment Neuron](Sentiment Neuron.md)
>   - Linear model + L1 [[Lp Regularization]]
>
> - [Term](Regularization Term.md)
>   - [[Lp Regularization]] for p =2
>
> - [Cosine Similarity](Cosine Similarity.md)
>   - [[Lp Regularization]] l2norm aka p = 2
>
> - [Sparse Dict Learning [[loss|Loss]]](Sparse Dictionary Learning Loss.md)
>   - $\lambda \Sigma_i |r_i|$ is Lasso/L1 [[Lp Regularization]]
>
> - [FaceNet](FaceNet.md)
>   - squared [[Lp Regularization]] L2 distance, in the [[Embedding|embedding]] space directly correspond to face similarity: faces of the same person have small distances and faces of distinct people have large distances
>
> - [No Bias Decay](No bias decay.md)
>   - Equivalent to [[Lp Regularization]] L2 to all parameters to drive the values towards 0

_Backlinks last generated 2022-10-04 13:01:19_
