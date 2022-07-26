---
title: Cross Entropy
tags: loss
---

# Cross [[Entropy]]
- [[Entropy]]
- Cross-[[Entropy|entropy]] is a measure from the field of information theory, building upon [[Entropy|entropy]] and generally calculating the difference between two [[Probability]] [[distributions]]. 
- It is closely related to but is different from [[KL Divergence]] that calculates the relative [[Entropy|entropy]] between two [[Probability]] [[distributions]], whereas cross-[[Entropy|entropy]] can be thought to calculate the total [[Entropy|entropy]] between the [[Distributions.md|distributions]].
- implicit distribution $$p(Y|x;\theta)$$ -> use CE
- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} log (p_{model}(Y|x))$$
	- Categorical CE
		- Classification
		- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} \Sigma_{i=1}^C 1(y=i)log (p_{model}f_i(x|\theta))$$
		- C is no of classes
	- [[MSE]]
		- Regression
		- $$\mathscr{L}(\theta) = \frac{1}{2}\mathbb{E}_{(x,y) \sim P(X,Y)}||y-f(x;\theta)||^2$$


































































































## Backlinks

> - [BCE Logits](BCE with Logits.md)
>   - [[Cross Entropy]] + logits
>    
> - [Label Smoothing](Label Smoothing.md)
>   - During training, minimize negative [[Cross Entropy]] loss to make these [[Distributions.md|distributions]] similar
>    
> - [Focal Loss](Focal Loss.md)
>   - modulating term to [[Cross Entropy]] in order to focus learning on hard misclassified examples
>    
> - [KL Divergence](KL Divergence.md)
>   - [[Entropy]] + [[Cross Entropy]]
>    
> - [Distillation Loss](Distillation Loss.md)
>   - Negative [[Cross Entropy]] + other
>    
> - [Perplexity](Perplexity.md)
>   - This is also equivalent to the exponentiation of the [[Cross Entropy]] between the data and model predictions

_Backlinks last generated 2022-07-26 20:33:15_
