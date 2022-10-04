---
tags: temp
title: Detailed Balance
date modified: Thursday, August 11th 2022, 12:32:55 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Detailed Balance
- To find a transition kernel T(x|y) for a homogenous, [[Ergodic]] [[Markov Chain]]
- If we pick some state x with the [[Probability]] given by g and multiply its prob g(x) with the transition [[Probability]] [[Density|density]] T(x|y) (weighted by [[Probability]] [[Density|density]] of x) then its the same as the reverse weighted transiting [[Probability]] [[Density|density]] from y to x
- $$\forall x,y \in \mathbb{R}^{k}: T(y|x)g(x) = T(x|y)g(y)$$
- If T(x|y) has detailed balance wrt g, then it is an [[Invariant Distribution]]
- $$\int_{\mathbb{R}^{k}}T(x|y)g(y)dy = \int_{\mathbb{R}^{k}}T(y|x)g(x)dy = g(x)\int_{\mathbb{R}^{k}}P(y|x)dy = g(x)$$

## Backlinks

> - [MCMC [[Sampling]]](MCMC Sampling.md)
>   - [[Detailed Balance]]

_Backlinks last generated 2022-10-04 13:01:19_
