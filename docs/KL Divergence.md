---
title: KL Divergence
---

# KL Divergence
- Classification
- Entropy + [[Cross Entropy]]
- We first define xlogx for a weird edge case $$x \cdot \log\left( x \right)$$

Then entropy $$\mathrm{sum}\left( \mathrm{xlogx}\left( y \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

Then cce as defined before $$ - \mathrm{sum}\left( y \cdot \log\left( ŷ \right) \right)$$

Finally KLD $$entropy + crossentropyloss$$

 - $$KL(p,q) = \Sigma_x p(x) log\frac{p(x)}{q(x)}$$

## Backlinks
* [[Loss Functions]]
	* [[KL Divergence]]
* [[Variational Autoencoder]]
	* Eg: By Loss func [[KL Divergence]] and prob distribution $$L(X) = n^{-1}\\Sigma*i||x*i - D(E(\\tilde x))||^2 + \\lambda \\cdot KL(f_i, d)$$

## …
