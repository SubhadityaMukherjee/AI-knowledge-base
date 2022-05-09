---
title: N Dim Normal Distribution
tags: distribution
---

# N Dim [[Normal Distribution]]
- [[Normal Distribution]]
- If data points are vectors $x = (x_{1}, …, x_{n})'$ and RVs X_i fulfill the [[Central Limit Theorem]],
- [[PDF]] $$p(x) = \frac{1}{(2\pi)^{n/2}det(\Sigma)^{\frac{1}{2}}}exp\left(-\frac{1}{2}(x-\mu)'\Sigma^{-1}(x-\mu)\right)$$
- $\mu$ is expectation $E[(X_{1}, …, X_{n})']$ and $\Sigma$ is the covariance matrix
- $$\Sigma(i,j) = E[(X_{i} - E[X_{i}])(X_{j}-E[X_{j}])]$$
- ![[Pasted image 20220319151038.png]]
- $$\hat \mu = \frac{1}{N}\Sigma_{i}x_{i}$$ and $$\hat \Sigma = \frac{1}{N-1}\Sigma_{i}(x_{i}-\hat\mu)(x_{i}-\hat\mu)'$$


































