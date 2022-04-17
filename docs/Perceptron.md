---
title: Perceptron
---

# Perceptron
- $$f(x)=sign(\Sigma _i w_ix_i +b) = sign(\mathbf{w^Tx}+b)$$
	- $$sign(x) = \begin{cases} 1 & x\geq0 \\ 0 & otherwise\end{cases}$$
![[Pasted image 20220304121008.png]]
- computational graph![[Pasted image 20220304121221.png]]
- Multi layer
	- Stack multiple perceptrons
	- $$\begin{align} \\& h_0 = x h1= sign(\mathbf{w_1^T}+b_1) \\ &…\\& h1= sign(\mathbf{w_{L-1}^T}+b_L) \end{align}$$







## Backlinks
* [[Layers]]
	* [[Perceptron]]

