---
title: Window Based Regression
tags: architecture 
---

# Window Based Regression
- [[TIme Series]]
- input window : $$u(t-d+1), u(t-d+2), …. , u(t-1) , u(t)$$
- Require regression function $$f:(\mathbb{R}^k)^d \rightarrow \mathbb{R}^m$$
	- $$k \times d$$  dim matrix
	- Flatten into $$d \cdot k$$ vector and apply [[Quadratic Loss]]

## Non Linearity
- Add fixed nonlinear transforms to input arguments : eg polynomials
- [[Volterra expansion]]


































































































## Backlinks

> - [Linear Regression](LinearRegression.md)
>   - [[Window Based Regression]]

_Backlinks last generated 2022-07-26 20:33:15_
