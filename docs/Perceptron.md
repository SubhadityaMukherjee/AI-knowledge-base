---
tags: temp
title: Perceptron
tag: architecture
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Perceptron
- $$f(x)=sign(\Sigma _i w_ix_i +b) = sign(\mathbf{w^Tx}+b)$$
	- $$sign(x) = \begin{cases} 1 & x\geq0 \\ 0 & otherwise\end{cases}$$
![[assets/Pasted image 20220304121008.png|im]]
- computational graph![[assets/Pasted image 20220304121221.png|im]]
- Multi layer
	- Stack multiple perceptrons
	- $$\begin{align} \\& h_0 = x h1= sign(\mathbf{w_1^T}+b_1) \\ &…\\& h1= sign(\mathbf{w_{L-1}^T}+b_L) \end{align}$$

## Backlinks
> - [Heaviside](Heaviside.md)
>   - used in Rosenblatt's [[Perceptron]]
>
> - [Features](Features.md)
>   - 1 hidden layer [[Perceptron]] -> Universal fn estimator

_Backlinks last generated 2022-10-04 13:01:19_
