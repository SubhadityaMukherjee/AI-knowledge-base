---
title: Matrix notation for NNs
toc: true
categories:
  - deeplearning
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Matrix notation for NNs
```toc
```
## Example for simple case
- ![[Pasted image 20240827205806.png]]
- A NN consists of linear transformations alternating with [[loss]] functions.
- ![[Pasted image 20240827204853.png]]
- or , $$\begin{align*}
\mathbf{h = a[\theta_{0}+ \theta_{x}]} \\
\mathbf{h' = a[\psi_{0} + \Psi h]}\\
\mathbf{y' = \phi'_{0}+ \phi'h'}
\end{align*}$$
	- where  $\mathbf{a[\bullet]}$ 

## General case
- Vector of hidden units at layer $k$ is $h_k$ 
- Vector of biases that contribute to hidden layer $k+1$ is $\beta_{k}$ 
- Weights that are applied to $k^{th}$ layer and contribute to hidden layer $(k+1)^{th}$ is $\Omega_{k}$ 
- General network $y = f[x, \phi]$  with $K$ layers is now
- ![[Pasted image 20240827210048.png]]