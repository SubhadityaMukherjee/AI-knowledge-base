---
title: Label Smoothing
tags: regularize 
date modified: Thursday, August 11th 2022, 12:32:51 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Label Smoothing
- [[Dense]] layer is generally the last one and combined with soft max leads to a [[Probability]] distribution
- Assume true label to be y, then a truth [[Probability]] distribution would be $p_i=1$ If i=y and 0 otherwise
- During training, minimize negative [[Cross Entropy]] loss to make these [[Distributions.md|distributions]] similar
- We know, $$\mathscr{l}(p,q) = -log p_y = -z_y + log(\Sigma^{K}_{i=1}exp(z_i))$$
- Where the optimal solution is $z^{\ast}_{y}=\inf$
	- The output scores are encouraged to be distinctive which leads to overfitting
	- Leads to
- Instead $$\cases{1-\epsilon& if i=1\\\frac{\epsilon}{(K-1)} & \text{otherwise}}$$
- The optimal Solution is
	- $log((K-1)(1-\epsilon)/ \epsilon)+\alpha$ if $i=y$
	- $\alpha$ otherwise
		- Any real number
		- Finite output from the last layer that generalizes well
- If $\epsilon =0$ , $log((k-1)\frac{1-\epsilon}{\epsilon})$ is $\infty$
- As $\epsilon$ increases, the gap decreases
- If $\epsilon=\frac{K-1}{K}$, all optimizal $z^{\ast}_{i}$ are identical

## Backlinks

> - [ConvNeXt](ConvNeXt.md)
>   - extending the number of epochs, using [[AdamW]] optimizer, Stochastic Depth, [[Label Smoothing]]

_Backlinks last generated 2022-10-04 13:01:19_
