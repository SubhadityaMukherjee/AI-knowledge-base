---
title: Sampler
tags: distribution 
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sampler
- Given :
	- $P_{X}$ is a distribution on a measure space (E,B)
	- A seq of $X_{1}, X_{2}, …$ of random variables is a sampler if for all $A \in B$
	- $$P_{X}(A) = lim_{N \rightarrow \infty} \frac{1}{N}\Sigma_{i=1}^{N}1_{A}\circ X_{i}$$
	- $1_A$ is an indicator function for A
- $X_{1}, X_{2}, …$ need not have the same distribution or need to be independant
- Dream : All $X_{i}$ are uniformly distributed on [0,1]. (Impossible)

## Backlinks
> - [MCMC [[Sampling]]](MCMC Sampling.md)
>   - Sufficient but not necessary for [[Markov Chain]] to be a [[Sampler]] for g
>
> - [Uniform [[Sampling]]](Uniform Sampling.md)
>   - Random [[Sampler]]
>   - If need to sample from another distribution with a [[PDF]] f(x). Can use a uniform [[Sampler]] on the distribution [0,1] to indirectly sample from it
>   - Get a [[Sampler]] for by $$X_{i} = \varphi^{-1}\circ U_{i}$$

_Backlinks last generated 2022-10-04 13:01:19_
