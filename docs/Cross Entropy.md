---
title: Cross Entropy
---

# Cross Entropy
- [[Entropy]]
- Cross-entropy is a measure from the field of information theory, building upon entropy and generally calculating the difference between two probability distributions. 
- It is closely related to but is different from KL divergence that calculates the relative entropy between two probability distributions, whereas cross-entropy can be thought to calculate the total entropy between the distributions.
- implicit distribution $$p(Y|x;\theta)$$ -> use CE
- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} log (p_{model}(Y|x))$$
	- Categorical CE
		- Classification
		- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} \Sigma_{i=1}^C 1(y=i)log (p_{model}f_i(x|\theta))$$
		- C is no of classes
	- MSE
		- Regression
		- $$\mathscr{L}(\theta) = \frac{1}{2}\mathbb{E}_{(x,y) \sim P(X,Y)}||y-f(x;\theta)||^2$$

## Backlinks
* [[KL Divergence]]
	* Entropy + [[Cross Entropy]]
* [[Loss Functions]]
	* [[Cross Entropy]]
* [[BCE Logits]]
	* [[Cross Entropy]] + logits

## …
