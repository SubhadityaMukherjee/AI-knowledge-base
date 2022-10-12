---
title: Window Based Regression
tags: architecture 
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Window Based Regression
- [[TIme Series]]
- input window : $$u(t-d+1), u(t-d+2), …. , u(t-1) , u(t)$$
- Require regression function $$f:(\mathbb{R}^k)^d \rightarrow \mathbb{R}^m$$
	- $$k \times d$$ dim matrix
	- Flatten into $$d \cdot k$$ vector and apply [[Quadratic Loss]]

## Non Linearity
- Add fixed nonlinear transforms to input arguments : eg polynomials
- [[Volterra expansion]]

## Backlinks
> - [Linear Regression](LinearRegression.md)
>   - [[Window Based Regression]]

_Backlinks last generated 2022-10-04 13:01:19_
