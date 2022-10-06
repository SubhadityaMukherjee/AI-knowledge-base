---
title: KL Divergence
tags: loss
date modified: Thursday, October 6th 2022, 1:18:04 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# KL Divergence
- Classification
- [[Entropy]] + [[Cross Entropy]]
- Distribution Based metric
- Measures difference between two [[PDF]]
- We first define xlogx for a weird edge case $$x \cdot \log\left( x \right)$$

Then [[Entropy|entropy]] $$\mathrm{sum}\left( \mathrm{xlogx}\left( y \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

Then cce as defined before $$ - \mathrm{sum}\left( y \cdot \log\left( ŷ \right) \right)$$

Finally KLD $$entropy + crossentropyloss$$

 - $$KL(p,q) = \Sigma_x p(x) log\frac{p(x)}{q(x)}$$

## Backlinks
> - [Variational Autoencoder](VAE.md)
>   - Eg: By [[loss|Loss]] func [[KL Divergence]] and prob distribution $$L(X) = n^{-1}\Sigma_i||x_i - D(E(\tilde x))||^2 + \lambda \cdot KL(f_i, d)$
>
> - [Proxy Objective](Proxy Objective.md)
>   - [[KL Divergence]] $P' || P$ measures how much optimization is done
>
> - [Cross [[Entropy]]](Cross Entropy.md)
>   - It is closely related to but is different from [[KL Divergence]] that calculates the relative [[Entropy|entropy]] between two [[Probability]] [[distributions]], whereas cross-[[Entropy|entropy]] can be thought to calculate the total [[Entropy|entropy]] between the [[Distributions.md|distributions]].

_Backlinks last generated 2022-10-04 13:01:19_
