---
title: Batch Normalization
tags: regularize
---

# Batch Normalization
- bias=False for Linear/Conv2D for input and True for output #tricks
- Normalizes #activations
- Input [distributions](distributions) change per layer -> Make sure they stay similar
- Reduces co variate shift because now the network must adapt per layer
- During testing : use stats saved during training
- Simplifies learning dynamics
	- Can use larger learning rate
	- Higher order interactions are suppressed because the mean and std are independant of the activations which makes training easier
- Cant work with small batches. Not great with RNN
- ![im](assets/Pasted%20image%2020220306114903.png)
- $$\mu_j \leftarrow \frac{1}{m}\Sigma_{i=1}^m x_{ij}$$
- $$\sigma^2_j \leftarrow \frac{1}{m}\Sigma^m_{i=1}(x_{ij}-\mu_j)^2$$
- $$\hat x_{ij} \leftarrow \frac{x_{ij}-\mu_j}{\sqrt{\sigma^2_j + \epsilon}}$$
- $$\hat x_{ij} \leftarrow \gamma \hat x_{ij} + \beta$$


































































































