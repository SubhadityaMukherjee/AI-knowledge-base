---
title: Detailed Balance
---

# Detailed Balance
- To find a transition kernel T(x|y) for a homogenous, [[Ergodic]] [[Markov Chain]]
- If we pick some state x with the [[Probability]] given by g and multiply its prob g(x) with the transition [[Probability]] density T(x|y) (weighted by [[Probability]] density of x)  then its the same as the reverse weighted transiting [[Probability]] density from y to x
- $$\forall x,y \in \mathbb{R}^{k}: T(y|x)g(x) = T(x|y)g(y)$$
- If T(x|y) has detailed balance wrt g, then it is an [[Invariant Distribution]]
- $$\int_{\mathbb{R}^{k}}T(x|y)g(y)dy = \int_{\mathbb{R}^{k}}T(y|x)g(x)dy = g(x)\int_{\mathbb{R}^{k}}P(y|x)dy = g(x)$$


































































































## Backlinks

> - [MCMC [[Sampling]]](MCMC Sampling.md)
>   - [[Detailed Balance]]

_Backlinks last generated 2022-07-26 20:33:15_
