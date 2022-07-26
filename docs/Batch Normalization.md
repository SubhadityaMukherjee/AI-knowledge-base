---
title: Batch Normalization
tags: regularize
---

# Batch Normalization
- bias=False for Linear/Conv2D for input and True for output #tricks
- Normalizes #activations
- Input [[distributions]] change per layer -> Make sure they stay similar
- Reduces co variate shift because now the network must adapt per layer
- During testing : use stats saved during training
- Simplifies learning dynamics
	- Can use larger learning rate
	- Higher order interactions are suppressed because the mean and std are independant of the activations which makes training easier
- Cant work with small batches. Not great with RNN
- ![[assets/Pasted image 20220306114903.png|im]]
- $$\mu_j \leftarrow \frac{1}{m}\Sigma_{i=1}^m x_{ij}$$
- $$\sigma^2_j \leftarrow \frac{1}{m}\Sigma^m_{i=1}(x_{ij}-\mu_j)^2$$
- $$\hat x_{ij} \leftarrow \frac{x_{ij}-\mu_j}{\sqrt{\sigma^2_j + \epsilon}}$$
- $$\hat x_{ij} \leftarrow \gamma \hat x_{ij} + \beta$$


































































































## Backlinks

> - [ConvNeXt](ConvNeXt.md)
>   - [[GELU]] instead of [[Relu]] , a single activation for each block (the original [[Transformer]] module has just one activation after the MLP), fewer normalization [[Layers]], [[Batch Normalization]] substituted by [[Layer Normalization]] , and separate downsampling layer
>    
> - [Non [[Relational Inductive Bias]]](Non Relational Inductive Bias.md)
>   - [[Batch Normalization]] , [[Layer Normalization]] , [[Instance Normalization]]
>    
> - [Large Batch Training](Large Batch Training.md)
>   - Modified [[Batch Normalization]] with $\gamma=0$ for all BNs at the end of a residual block that micmics networks with less [[Layers]] and is easier to train at the start
>    
> - [Regularization](Regularization.md)
>   - [[Batch Normalization]]
>    
> - [Layer Normalization](Layer Normalization.md)
>   - ![[assets/Pasted image 20220621163906.jpg]] (Compared to [[Batch Normalization]])
>    
> - [Inception](Inception.md)
>   - Added [[Batch Normalization]]
>    
> - [No Bias Decay](No bias decay.md)
>   - Leave [[Batch Normalization]] [[Layers]] alone
>    
> - [Xavier [[Initialization]]](Xavier Initialization.md)
>   - For [[Batch Normalization]] [[Layers]], $\gamma =1$ and $\beta=0$

_Backlinks last generated 2022-07-26 20:33:15_
