---
title: Sigmoid
tags: architecture 
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sigmoid
- $$\sigma(x) = \frac{1}{1+exp(-x)}$$
- $$\frac{d\sigma}{dx}(x) = \sigma(x)(1-\sigma(x))$$
	- max : 0.25
- Logistic
- Xavier/Glorot init
- RNN : Hidden
- [[Bernoulli Distribution]] over a binary variable
- ![[assets/Pasted image 20220626151646.jpg]]

## Backlinks
> - [Universal Approximation Theorem](Universal Approximation Theorem.md)
>   - So we take a non linear function, for example the [[Sigmoid]]. $$\frac{1}{1 + e^{ - \left( w^{T}x + b \right)}}$$.
>
> - [FTSwish](FTSwish.md)
>   - [[Relu]] + [[Sigmoid]]
>
> - [He Initialization](He Initialization.md)
>   - For [[Sigmoid]] based activation functions
>
> - [Gated [[Recurrent]] Unit (GRU)](Gated Recurrent Unit (GRU).md)
>   - Two gates, [[Sigmoid]]
>
> - [](ActivationFunctions.md)
>   - [[SELU]] > [[Elu]] > [[Leaky Relu]] > [[Relu]] > [[Tanh]] > [[Sigmoid]]
>
> - [[[Uncertainty]] Classification](Uncertainity in classification.md)
>   - Use [[Softmax]] or [[Sigmoid]]
>
> - [Recurrent](Recurrent.md)
>   - Activation usually [[Sigmoid]] or [[Tanh]]

_Backlinks last generated 2022-10-04 13:01:19_
