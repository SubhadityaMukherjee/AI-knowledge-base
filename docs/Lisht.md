---
title: Lisht

tags: activations 
date modified: Thursday, August 11th 2022, 12:32:51 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Lisht
- ![[assets/Pasted image 20220625234951.png]]
- Derivatives
	- ![[assets/Pasted image 20220625234959.png]]
- [blog](https://github.com/christianversloot/machine-learning-articles/blob/main/beyond-swish-the-lisht-activation-function.md) #[[Roam-Highlights]]
    - Linearly Scaled Hyperbolic Tangent
    - his activation function simply uses the [[Tanh]] function and scales it linearly, as follows
    - $$LiSHT(x) = x \times tanh(x)$$
    - Essentially, LiSHT looks very much like [[Swish]] in terms of the first-order derivative. However, the range is expanded into the negative as well, which means that the vanishing gradient problem is reduced even further - at least in theory.
    - In their work, Roy et al. (2019) report based on empirical testing that indeed, the vanishing gradient problems is reduced compared to [[Swish]] and traditional [[Relu|ReLU]]. Additional correlations between network learning and the shape of e.g. the LiSHT loss landscape were identified.

## Backlinks

> - [Swish](Swish.md)
>   - Move to [[Lisht]]

_Backlinks last generated 2022-10-04 13:01:19_
