---
title: Contrastive Loss
tags: loss
---

# Contrastive Loss
- Minimize distance between similar inputs [[Gradient Descent gradients]], maximize between dissimilar [[Gradient Ascent]]
- Learn Embedding/Feature space using neighbors
- dim(Embedding d) < dim(input Space D)
- Encoded using a learnable function(NN) $$G_\theta(x) : \mathcal{R}^D \rightarrow \mathcal{R}^d$$
- Binary labels : similar or not
- $$D_\theta(x_1, x_2) = ||G_\theta(x_1) - G_\theta(x_2)||_2$$
- $$L(\theta, y, x_1, x_2) = \frac{(1-y)(D_\theta(x_1, x_2))^2}{2} + \frac{y(max(0,m-D\theta(x_1, x_2)))^2}{2}$$
	- m is enforced margin between similar and dissimilar (m>0)
	- Labeled points $$(y,x_1,x_2)$$ are generated
































