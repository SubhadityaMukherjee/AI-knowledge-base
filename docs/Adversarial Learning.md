---
tags: temp
title: Adversarial Learning
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Adversarial Learning
- Consider data in a [[Manifold]]. The [[PDF]] is concentrated along a low dim [[Manifold]] $\mathcal{M}$
- Now the original picture is a point on the [[Manifold]] (dim = output layer size)
- Add noise to the image such that the image now appears to be in a direction orthogonal to $\mathcal{M}$ -> value of [[PDF]] shrinks dramatically
- Then the network has never seen this before and will return a random classification

## Backlinks
> - [Generalizing Adversarial Explanations with Grad-CAM](Generalizing Adversarial Explanations with Grad-CAM.md)
>   - [[Adversarial Learning]]
>
> - [Visual Commonsense Reasoning](Visual Commonsense Reasoning.md)
>   - [[Adversarial Learning]]
>
> - [Manifold](Manifold.md)
>   - Can be exploited by [[Adversarial Learning]]
>
> - [GAN](Generative Models.md)
>   - [[Adversarial Learning]]

_Backlinks last generated 2022-10-05 15:25:18_
