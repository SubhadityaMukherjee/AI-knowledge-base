---
title: Softmax
tags: architecture 
---

# Softmax
- Output : probabilities
- $$p = \frac{1}{\Sigma_{i = 1, .., n}e^{\frac{\alpha y_{i}}{T}}}(e^{\frac{\alpha y_{1}}{T}} , e^{\frac{\alpha y_{2}}{T}} , …, e^{\frac{\alpha y_{n}}{T}})'$$
- Softer argmax (0,1)
- Multinoulli

## [Entropy](Entropy.md)
- $\alpha$ determines [entropy](Entropy.md)
- If it is 0, and [[uniform distribution]] and limit to infinity -> binary vector which is 0 everywhere except at position i when y is maximal

## Temperature
- Higher the T -> Softer it the distribution. Aka less confident about distribution
- Lower -> Harder. More confident


























































## Backlinks

> - [Uncertainty](Uncertainty.md)
>   - Most networks are overconfident - [[Softmax]] confidences do not have a good probabilistic interpretation. Wrong predictions with more confidence
>    
> - [Recurrent](Recurrent.md)
>   - [[Softmax]] but on every output vector simultaneously
>    
> - [Activation Functions](ActivationFunctions.md)
>   - [[Softmax]]
>    
> - [Scaled [Dot Product Attention](Dot%20Product%20Attention.md)](Scaled Dot Product Attention.md)
>   - [[Softmax]] is sensitive to large values. Which sucks for the #gradients
>    
> - [Self Attention](Self Attention.md)
>   - Any value between -inf to +inf so [[Softmax]] is applied
>    
> - [Distillation Loss](Distillation Loss.md)
>   - T is the temperature to make [[Softmax]] smoother
>    
> - [[[Uncertainty]] Classification](Uncertainity in classification.md)
>   - Use [[Softmax]] or [[Sigmoid]]

_Backlinks last generated 2022-06-24 12:00:32_
