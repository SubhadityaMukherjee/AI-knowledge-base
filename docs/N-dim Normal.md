---
title: N Dim Normal Distribution
tags: distribution
---

# N Dim [Normal Distribution](Normal%20Distribution.md)
- [Normal Distribution](Normal%20Distribution.md)
- If data points are vectors $x = (x_{1}, …, x_{n})'$ and RVs X_i fulfill the [Central Limit Theorem](Central%20Limit%20Theorem.md),
- [PDF](PDF.md) $$p(x) = \frac{1}{(2\pi)^{n/2}det(\Sigma)^{\frac{1}{2}}}exp\left(-\frac{1}{2}(x-\mu)'\Sigma^{-1}(x-\mu)\right)$$
- $\mu$ is expectation $E[(X_{1}, …, X_{n}|[X_{1}, …, X_{n})'](Covariance.md)']] matrix
- $$\Sigma(i,j) = E[(X_{i} - E[X_{i}])(X_{j}-E[X_{j}])]$$
- ![im](assets/Pasted%20image%2020220319151038.png)
- $$\hat \mu = \frac{1}{N}\Sigma_{i}x_{i}$$ and $$\hat \Sigma = \frac{1}{N-1}\Sigma_{i}(x_{i}-\hat\mu)(x_{i}-\hat\mu)'$$


































































































