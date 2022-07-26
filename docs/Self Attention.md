---
title: Self Attention
tags: architecture einsum 
---

# Self [[Attention]]
- [paper](https://arxiv.org/abs/1706.03762v5)
- Basically [[Scaled Dot Product Attention]]
- Q,K,V all from same module but prev layer
- Weighted average over all input vectors $$y_{i}= \Sigma_{j}w_{ij}x_{j}$$
	- j is over the sequence
	- weights sum to 1 over j
	- $w_{ij}$ is derived  $w^{'}_{ij}=x_{i}^{T}x_{j}$
		- Any value between -inf to +inf so [[Softmax]] is applied
	- $x_i$ is the input vector at the same pos as the current output vector $y_i$
- Propagates info between vectors
- ![[assets/Pasted image 20220525183444.png|im]]
- The process
	- Assign every word t in the vocabular an [[Embedding]]
	- Feeding this into a self [[Attention|attention]] layer we get another seq of vectors $y_{the}$ , $y_{cat}$ etc
	- each of the $y_{something}$ is a weighted sum over all the [[Embedding|embedding]] vectors in the first seq weighted by their normalized dot product with $v_{something}$
	- the dot product shows how related the vectors are in the sequence
		- weights determined by them
		- Self-[[Attention]] layer may give more weights to those input vectors that are more similar to each other when generating the output vectors
- Properties
	- Inputs are a set (not sequence)
	- If input seq is permuted, the output is too
	- Ignores the sequential nature of input by itself
- Code

```python
def attention(K, V, Q):
    _, n_channels, _ = K.shape
    A = torch.einsum('bct,bcl->btl', [K, Q])
    A = F.softmax(A * n_channels ** (-0.5), 1)
    R = torch.einsum('bct,btl->bcl', [V, A])
    return torch.cat((R, Q), dim=1)
```

## Ref
- [perterbloem](https://peterbloem.nl/blog/transformers)


























