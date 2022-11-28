---
title: Softmax
tags: architecture 
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Softmax
- Output : probabilities
- $$p = \frac{1}{\Sigma_{i = 1, .., n}e^{\frac{\alpha y_{i}}{T}}}(e^{\frac{\alpha y_{1}}{T}} , e^{\frac{\alpha y_{2}}{T}} , …, e^{\frac{\alpha y_{n}}{T}})'$$
- Softer argmax (0,1)
- Multinoulli

## [Entropy](Entropy.md)
- $\alpha$ determines [entropy](Entropy.md)
- If it is 0, and [Uniform_Distribution](Uniform_Distribution.md) and limit to infinity -> binary vector which is 0 everywhere except at position i when y is maximal

## Temperature
- Higher the T -> Softer it the distribution. Aka less confident about distribution
- Lower -> Harder. More confident
- ![softmax_logits](images/softmax_logits.webp)

## Backlinks

> - [Declarative Memory Blending](Declarative Memory Blending.md)
>   - [[Softmax]]

_Backlinks last generated 2022-11-28 14:44:43_
