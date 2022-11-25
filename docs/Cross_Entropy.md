---
title: Cross Entropy
tags: loss
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cross [Entropy](Entropy.md)
- [Entropy](Entropy.md)
- Cross-[entropy](Entropy.md) is a measure from the field of information theory, building upon [entropy](Entropy.md) and generally calculating the difference between two [Probability](Probability.md) [distributions](distributions).
- It is closely related to but is different from [KL_Divergence](KL_Divergence.md) that calculates the relative [entropy](Entropy.md) between two [Probability](Probability.md) [distributions](distributions), whereas cross-[entropy](Entropy.md) can be thought to calculate the total [entropy](Entropy.md) between the [distributions](Distributions.md).
- implicit distribution $$p(Y|x;\theta)$$ -> use CE
- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} log (p_{model}(Y|x))$$
	- Categorical CE
		- Classification
		- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} \Sigma_{i=1}^C 1(y=i)log (p_{model}f_i(x|\theta))$$
		- C is no of classes
	- [MSE](MSE.md)
		- Regression
		- $$\mathscr{L}(\theta) = \frac{1}{2}\mathbb{E}_{(x,y) \sim P(X,Y)}||y-f(x;\theta)||^2$

