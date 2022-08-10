---
title: Softmax
tags: architecture 
date modified: Wednesday, August 10th 2022, 11:41:23 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Softmax
- Output : probabilities
- $$p = \frac{1}{\Sigma_{i = 1, .., n}e^{\frac{\alpha y_{i}}{T}}}(e^{\frac{\alpha y_{1}}{T}} , e^{\frac{\alpha y_{2}}{T}} , …, e^{\frac{\alpha y_{n}}{T}})'$$
- Softer argmax (0,1)
- Multinoulli

## [Entropy](Entropy.md)
- $\alpha$ determines [entropy](Entropy.md)
- If it is 0, and [Uniform Distribution](Uniform%20Distribution.md) and limit to infinity -> binary vector which is 0 everywhere except at position i when y is maximal

## Temperature
- Higher the T -> Softer it the distribution. Aka less confident about distribution
- Lower -> Harder. More confident
- ![softmax_logits](assets/softmax_logits.webp)

## Backlinks

> - [Generative RNN](Generative RNN.md)
>   - normally not taking argmax but sample with respective [[Softmax]] probabilities -> allows to generate something different than input
>    
> - [MLM (Masked Language Modeling)](MLM.md)
>   - calculating probability of each word in the vocabulary using [[Softmax]]

_Backlinks last generated 2022-08-10 16:56:31_
