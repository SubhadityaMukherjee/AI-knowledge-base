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

## [[Entropy]]
- $\alpha$ determines [[Entropy|entropy]]
- If it is 0, and [[Uniform Distribution]] and limit to infinity -> binary vector which is 0 everywhere except at position i when y is maximal

## Temperature
- Higher the T -> Softer it the distribution. Aka less confident about distribution
- Lower -> Harder. More confident
- ![[assets/softmax_logits.webp]]

## Backlinks
> - [Distillation Loss](Distillation Loss.md)
>   - T is the temperature to make [[Softmax]] smoother
>
> - [Dot Product [[Attention]]](Dot Product Attention.md)
>   - Final scores after [[Softmax]]
>
> - [Self [[Attention]]](Self Attention.md)
>   - Any value between -inf to +inf so [[Softmax]] is applied
>
> - [[[Attention]] Alignment](Attention Alignment.md)
>   - Final scores calculated with a [[Softmax]]
>
> - [Scaled [[Dot Product Attention]]](Scaled Dot Product Attention.md)
>   - [[Softmax]] is sensitive to large values. Which sucks for the #gradients
>
> - [Generative RNN](Generative RNN.md)
>   - normally not taking argmax but sample with respective [[Softmax]] probabilities -> allows to generate something different than input
>
> - [[[Uncertainty]] Classification](Uncertainity in classification.md)
>   - Use [[Softmax]] or [[Sigmoid]]
>
> - [Recurrent](Recurrent.md)
>   - [[Softmax]] but on every output vector simultaneously
>
> - [MLM (Masked Language Modeling)](MLM.md)
>   - calculating probability of each word in the vocabulary using [[Softmax]]

_Backlinks last generated 2022-10-04 13:01:19_
