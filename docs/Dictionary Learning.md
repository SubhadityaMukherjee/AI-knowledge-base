---
title: Dictionary Learning
---

# Dictionary Learning
- Given : N unlabeled data points $$x_i \in \mathcal{R}^d$$
- To find:
	- Linear rep of these points based on set of basis vectors
		- $$x = \Sigma_i^k r_i \cdot d_i = Dr$$
		- dimension d
		- r are repr weights corresponding to basis vector d
		- D is a dict with basis vectors
		- R contains weights. Scalar
		- $$||d_i|| \leq 1$$
- [[Sparse Dictionary Learning Loss]]

- After learning, these can be used as discriminative features
	- Expensive to compute










































