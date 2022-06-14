---
title: Scaled Dot Product Attention
tags: architecture 
---

# Scaled Dot Product Attention
- Q is query, K is key V is value. Same dims
- $q_{i}= W_{q}x_i$ ,  $k_{i}= W_{k}x_{i}$ ,  $v_{i}= W_{v}x_{i}$
	- $w_{ij}' = q_{i}^{T}k_{j}$ 
	- $y_{i}= \Sigma_{j}w_{ij}v_{j}$
- [[Softmax]] is sensitive to large values. Which sucks for the #gradients 
- The avg value of the dot product grows with embedding dimension k. So scale back.
	- $\sqrt{k}$ . Vector in $\mathbb{R}^{k}$  with all values as c
	- Euclidean length is $\sqrt{kc}$
- $$Attention(Q, K,V) = softmax(\frac{QK^T}{\sqrt{K}})V$$
- Generalization of [[soft attention]]
- ![[Pasted image 20220526133045.png]]




