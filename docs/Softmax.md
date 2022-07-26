---
title: Softmax
tags: architecture 
---

# Softmax
- Output : probabilities
- $$p = \frac{1}{\Sigma_{i = 1, .., n}e^{\frac{\alpha y_{i}}{T}}}(e^{\frac{\alpha y_{1}}{T}} , e^{\frac{\alpha y_{2}}{T}} , …, e^{\frac{\alpha y_{n}}{T}})'$$
- Softer argmax (0,1)
- Multinoulli

## [[Entropy]]
- $\alpha$ determines [[Entropy|entropy]]
- If it is 0, and [[Uniform Distribution]] and limit to infinity -> binary vector which is 0 everywhere except at position i when y is maximal

## Temperature
- Higher the T -> Softer it the distribution. Aka less confident about distribution
- Lower -> Harder. More confident
- ![[assets/softmax_logits.webp]]




























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
> - [Scaled [[Dot Product Attention]]](Scaled Dot Product Attention.md)
>   - [[Softmax]] is sensitive to large values. Which sucks for the #gradients
>    
> - [Self [[Attention]]](Self Attention.md)
>   - Any value between -inf to +inf so [[Softmax]] is applied
>    
> - [Distillation Loss](Distillation Loss.md)
>   - T is the temperature to make [[Softmax]] smoother
>    
> - [Dot Product [[Attention]]](Dot Product Attention.md)
>   - Final scores after [[Softmax]]
>    
> - [[[Uncertainty]] Classification](Uncertainity in classification.md)
>   - Use [[Softmax]] or [[Sigmoid]]
>    
> - [[[Attention]] Alignment](Attention Alignment.md)
>   - Final scores calculated with a [[Softmax]]

_Backlinks last generated 2022-07-26 20:33:15_
