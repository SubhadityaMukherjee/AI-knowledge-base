---
title: Scaled Dot Product Attention
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:46 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Scaled [[Dot Product Attention]]
- [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
- Q is query, K is key V is value. Same dims
- $q_{i}= W_{q}x_i$ , $k_{i}= W_{k}x_{i}$ , $v_{i}= W_{v}x_{i}$
	- $w_{ij}' = q_{i}^{T}k_{j}$
	- $y_{i}= \Sigma_{j}w_{ij}v_{j}$
- [[Softmax]] is sensitive to large values. Which sucks for the #gradients
- The avg value of the dot product grows with [[Embedding|embedding]] dimension k. So scale back.
	- $\sqrt{k}$ . Vector in $\mathbb{R}^{k}$ with all values as c
	- Euclidean length is $\sqrt{kc}$
- $$Attention(Q, K,V) = softmax(\frac{QK^T}{\sqrt{d_{k}}})V$$
- Generalization of [[Soft Attention]]
- ![[assets/Pasted image 20220526133045.png|im]]
- [[Attention Alignment]] score $$\alpha_{t,i} = \frac{s_{t}^{T}h_{i}}{\sqrt{n}}$$

## Backlinks

> - [Self [[Attention]]](Self Attention.md)
>   - Basically [[Scaled Dot Product Attention]]
>    
> - [Multiplicative [[Attention]]](Multiplicative Attention.md)
>   - Since [[Additive Attention]] performs better for scale, use a factor [[Scaled Dot Product Attention]]
>    
> - [Attention](Attention.md)
>   - [[Scaled Dot Product Attention]]

_Backlinks last generated 2022-10-04 13:01:19_
