---
title: KL Divergence
tags: loss
---

# KL Divergence
- Classification
- [Entropy](Entropy.md) + [Cross Entropy](Cross%20Entropy.md)
- We first define xlogx for a weird edge case $$x \cdot \log\left( x \right)$$

Then [entropy](Entropy.md) $$\mathrm{sum}\left( \mathrm{xlogx}\left( y \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

Then cce as defined before $$ - \mathrm{sum}\left( y \cdot \log\left( ŷ \right) \right)$$

Finally KLD $$entropy + crossentropyloss$$

 - $$KL(p,q) = \Sigma_x p(x) log\frac{p(x)}{q(x)}$$






























































































