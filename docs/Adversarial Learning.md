---
title: Adversarial Learning
---

# Adversarial Learning
- Consider data in a manifold. The pdf is concentrated along a low dim manifold $\mathcal{M}$
- Now the original picture is a point on the manifold (dim = output layer size)
- Add noise to the image such that the image now appears to be in a direction orthogonal to $\mathcal{M}$ -> value of pdf shrinks dramatically
- Then the network has never seen this before and will return a random classification





## Backlinks
* [[Manifold]]
	* Can be exploited by [[Adversarial Learning]]
