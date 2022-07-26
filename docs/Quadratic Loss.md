---
title: Quadratic Loss
tags: loss
---

# Quadratic Loss
- $$W = argmin_{W^{\ast}}\Sigma^N_{i=1} ||W^{\ast} x_i - y_i||^2$$
- $$\Delta : \mathbb{R}^{n} \rightarrow \mathbb{R}, x \rightarrow E[Y|X = x]$$ is the gold standard for minimizing this. But $\Delta$ is unknown


































































































## Backlinks

> - [Window Based Regression](Window Based Regression.md)
>   - Flatten into $$d \cdot k$$ vector and apply [[Quadratic Loss]]
>    
> - [Bias Vs Variance](Bias Variance Dilemma.md)
>   - [[Quadratic Loss]] (risk) is minimized by the function $$\Delta(x) = E_{Y|X=x}[Y]$$
>    
> - [Linear Regression](LinearRegression.md)
>   - [[Quadratic Loss]]

_Backlinks last generated 2022-07-26 20:33:15_
