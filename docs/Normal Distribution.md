---
title: Normal Distribution
tags: distribution
date modified: Thursday, August 11th 2022, 12:32:49 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Normal Distribution
- $$p(x) = \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$$
- Mean $\mu$ and std $\sigma$. $\mu$ is max and $\mu \pm \sigma$ is locations of zeros of second derivative
- ![[assets/Pasted image 20220319144034.png|im]]
- $\mathcal{N}(0,1)$
- [[Central Limit Theorem]]

## Properties
- Linear combinations of normal distributed independant RVs are normal distributed
- X,Y have means $\mu$ and v and variances $\sigma^{2}$ and $\tau^{2}$. Then $aX + bY$ is normally distributed and has mean : $a\mu + bv$ and variance $\alpha^{2}\sigma^{2}+b^{2}\tau^{2}$

## Computing the Value
- $$\int_{a}^{b} \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}dx$$
- Transform $\mathscr{N}(\mu, \sigma^{2})$ to $\mathscr{N}(0,1)$
- $$Z = \frac{X-\mu}{\sigma}$$
- $$\int_{\frac{a-\mu}{\sigma}}^{\frac{b-\mu}{\sigma}}\frac{1}{\sqrt{2\pi}}e^{-\frac{(x)^{2}}{2}}dx$$
- Compute by using Cumulative [[Density|density]] function $\phi$
- Iterative solvers
- $$\phi(\frac{b-\mu}{\sigma})-\phi(\frac{a-\mu}{\sigma})$$
- $$\hat \mu = \frac{1}{N}\Sigma_{i}(x_{i})$$ $$\hat \sigma^{2}= \frac{1}{N-1}\Sigma_{i}(x_{i}-\hat\mu)^2$$

## Backlinks

> - [Akaike Information Criterion](Akaike Information Criterion.md)
>   - If error terms $\epsilon$ follows [[Normal Distribution]] , expected value 0 + constant variance $$AIC = \frac{1}{\eta \sigma^{2}}(RSS + 2p \hat \sigma^2)$$
>    
> - [Central Limit Theorem](Central Limit Theorem.md)
>   - When random effects of many independant small sized causes sum up to large scale observable effects : one gets the [[Normal Distribution]]
>    
> - [N Dim [[Normal Distribution]]](N-dim Normal.md)
>   - # N Dim [[Normal Distribution]]
>   - [[Normal Distribution]]
>    
> - [Denoising Autoencoder](Denoising Autoencoder.md)
>   - [[Normal Distribution]]
>    
> - [Standard Deviation](Standard Deviation.md)
>   - [[Normal Distribution]]
>    
> - [GELU](GELU.md)
>   - $$x\Phi(x)$$ where $\Phi(x)$ is the [[Normal Distribution]] [[CDF]]

_Backlinks last generated 2022-10-04 13:01:19_
