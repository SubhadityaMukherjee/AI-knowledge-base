---
title: Quadratic Loss
tags: loss
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Quadratic [[loss|Loss]]
- $$W = argmin_{W^{\ast}}\Sigma^N_{i=1} ||W^{\ast} x_i - y_i||^2$
- $\Delta : \mathbb{R}^{n} \rightarrow \mathbb{R}, x \rightarrow E[Y|X = x]$ is the gold standard for minimizing this. But $\Delta$ is unknown

## Backlinks

> - [Linear Regression](LinearRegression.md)
>   - [[Quadratic Loss]]
>    
> - [Bias Vs Variance](Bias Variance Dilemma.md)
>   - [[Quadratic Loss]] (risk) is minimized by the function $$\Delta(x) = E_{Y|X=x}[Y]$$
>    
> - [Window Based Regression](Window Based Regression.md)
>   - Flatten into $$d \cdot k$$ vector and apply [[Quadratic Loss]]

_Backlinks last generated 2022-10-04 13:01:19_
