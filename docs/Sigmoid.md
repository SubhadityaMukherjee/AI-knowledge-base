---
title: Sigmoid
tags: architecture 
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

> - [FTSwish](FTSwish.md)
>   - [[Relu]] + [[Sigmoid]]
>    
> - [Recurrent](Recurrent.md)
>   - Activation usually [[Sigmoid]] or [[Tanh]]
>    
> - [Activation Functions](ActivationFunctions.md)
>   - [[Sigmoid]]
>    
> - [Universal Approximation Theorem](Universal Approximation Theorem.md)
>   - So we take a non linear function, for example the [[Sigmoid]]. $$\frac{1}{1 + e^{ - \left( w^{T}x + b \right)}}$$.
>    
> - [Gated [[Recurrent]] Unit (GRU)](Gated Recurrent Unit (GRU).md)
>   - Two gates, [[Sigmoid]]
>    
> - [[[Uncertainty]] Classification](Uncertainity in classification.md)
>   - Use [[Softmax]] or [[Sigmoid]]

_Backlinks last generated 2022-07-26 20:33:15_
