---
title: KL Divergence
tags: loss
date modified: Wednesday, September 14th 2022, 12:19:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# KL Divergence
- Classification
- [Entropy](Entropy.md) + [Cross Entropy](Cross%20Entropy.md)
- We first define xlogx for a weird edge case $$x \cdot \log\left( x \right)$$

Then [entropy](Entropy.md) $$\mathrm{sum}\left( \mathrm{xlogx}\left( y \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

Then cce as defined before $$ - \mathrm{sum}\left( y \cdot \log\left( ŷ \right) \right)$$

Finally KLD $$entropy + crossentropyloss$$

 - $$KL(p,q) = \Sigma_x p(x) log\frac{p(x)}{q(x)}$$

