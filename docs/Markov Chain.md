---
tags: temp
title: Markov Chain
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Markov Chain
- Sequence of random variables such as $X_{n+1}$ only depends on $X_{n}$
- Discrete time
- Stochastic process without memory
- Finite interval : [0, 1, … n]
- Right infinite : n = 1, 2, 3, …
- Left right infinite : Integers
	- No start
- [[Markov Initial Distribution]]
- [[Markov Transition Kernel]]
- [[Markov for Continuous Distributions]]

## Backlinks

> - [Invariant Distribution](Invariant Distribution.md)
>   - If g is the [[PDF]]. T(x|y) is the [[PDF]] of the transition kernel. Homogenous [[Markov Chain]]. Then g is [[PDF]] of an invariant distribution of T(x|y) if
>    
> - [Markov for Continuous Distributions](Markov for Continuous Distributions.md)
>   - If a [[Markov Chain]] with state set S, matrix M is executed m times . The transition probabilities transmit between states and then, $$P(X_{n+m}=s_{j}|X_{n}= s_{i}) = M^{m}(i, j)$$
>    
> - [MCMC [[Sampling]]](MCMC Sampling.md)
>   - [[Markov Chain]]
>   - Sufficient but not necessary for [[Markov Chain]] to be a [[Sampler]] for g
>    
> - [Markov Random Field](Markov Random Field.md)
>   - Generalized [[Markov Chain]]
>    
> - [Detailed Balance](Detailed Balance.md)
>   - To find a transition kernel T(x|y) for a homogenous, [[Ergodic]] [[Markov Chain]]
>    
> - [GAN](Generative Models.md)
>   - no need for any [[Markov Chain]] or unrolled approximate inference networks during either training or generation of samples

_Backlinks last generated 2022-10-04 13:01:19_
