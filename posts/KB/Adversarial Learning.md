---
categories: ['temp']
toc: true
title: Adversarial Learning
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Adversarial Learning
- Consider data in a [[Manifold.md|Manifold]]. The [[PDF.md|PDF]] is concentrated along a low dim [[Manifold.md|Manifold]] $\mathcal{M}$
- Now the original picture is a point on the [[Manifold.md|Manifold]] (dim = output layer size)
- Add noise to the image such that the image now appears to be in a direction orthogonal to $\mathcal{M}$ -> value of [[PDF.md|PDF]] shrinks dramatically
- Then the network has never seen this before and will return a random classification



