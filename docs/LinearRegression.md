---
title: Linear Regression
---

# Linear Regression
- Minimization problem $$(w,b) = argmin_{w^{\ast} , b^{\ast}} \Sigma^N_{i-1}(w^{\ast}x_{i} +b ^{\ast} - y_{i})^2$$
	- [[Affine Function]]
	- $$w = argmin_{w^\ast} || (\Sigma^n_{j = 1} w^\ast_j \phi_j) - y || ^2$$
		- w* is just $$(w^\ast_1 … w^\ast_n)$$
		- $$u_j$$ of U forms orthonormal basis of $$\mathscr{F}$$
- X : nxN matrix , y : N dim vector
- Solution : $$[w, b] \in \mathbb{R} ^{n+1}$$
- $$w' = (XX')^{-1}X y$$
	- If y is has vector data too (size k)
		- $$W' = (XX')^{-1}XY$$
		- Y : N x k matrix 
- ![[assets/Pasted image 20220309132129.png|im]]
- $$\phi _1  , \phi_2 …$$ form a subspace $$\mathscr{F}$$ with dim = n
	- linearly independant vectors. If not, drop as many as possible
- The optimal solution y_opt is the projection of y on that subspace and has the smallest distance from y
	- $$y_{opt} = w_1 \phi_1 + w_2 \phi_2$$
- $$(\Sigma^n_{j = 1} w^\ast_j \phi_j)$$ is a vector on $$\mathscr{F}$$

- [[Ridge Regression]]
- [[Window Based Regression]]

## General Defination
- Training data : $$(x_i, y_i)_{i= 1,..,N}$$ and $$\in \mathbb{R}^k$$ 
- Search space H
	- Candidate functions $$h: \mathbb{R}^n \rightarrow \mathbb{R}^k$$
- Loss function $$L : \mathbb{R}^k \times \mathbb{R}^k \rightarrow \mathbb{R}^{n \geq 0}$$
	- [[Quadratic Loss]]
- Solution : $$h_{opt} = argmin_{h \in \mathcal{H}}\Sigma_{i=1}^N L(h(x_i), y_i)$$
	- $$\mathcal{H}$$ is all linear functions from $$\mathbb{R}^n$$ to $$\mathbb{R}^k$$ 

## Random Notes
- $$(A'A)^{-1}A'$$ is the left psuedo inverse





































































## Backlinks

> - [Fundamentals](Fundamentals.md)
>   - [[LinearRegression]]
>    
> - [Inductive Bias](Inductive Bias.md)
>   - in [[LinearRegression]]
>    
> - [YOLO](YOLO.md)
>   - [[LinearRegression]] problem
>    
> - [Reg [[Uncertainty]]](Uncertainity in regression.md)
>   - [[LinearRegression]]
>    
> - [Dense](Dense.md)
>   - Weighted [[LinearRegression]]
>    
> - [Ridge Regression](Ridge Regression.md)
>   - [[LinearRegression]]
>    
> - [GloVE](GloVE.md)
>   - global log-bilinear [[LinearRegression]] model for the [[Unsupervised Learning|unsupervised learning]] of word representations
>    
> - [Methods for [[Feature Learning]]](Methods for Feature Learning.md)
>   - [[Gradient Descent gradients]] or [[LinearRegression]]

_Backlinks last generated 2022-07-26 20:33:15_
