---
title: Proxy Objective
tags: distribution 
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Proxy Objective
- Easier to change or measure than the actual objective
 - Suppose we have some sample space $S$ (such as the set of possible question-answer pairs), some [[Probability]] distribution $P$ over $S$, a true objective (or “reward”) $R_{true}: S \to \mathbb{R}$ , proxy objective $R_{proxy}:S \to \mathbb{R}$ and we optimize $R_{proxy}$ to get a new distribution $P'$
- $E_{x'\sim P'}[Rtrue(x′)]$ is how well the true objective is optimized
	- [[Monte Carlo]] estimator used
	- If $N \geq n$ samples from P, simultaneously consider every possible subset of these samples of size nnn, weight each sample by the number of subsets for which it is the best according to the proxy objective, and then take the weighted average true objective $$\binom{k-1}{n-1}$$ where k is the rank of the sample under the proxy objective, from 1 (worst) up to N (best)
	- Can reuse samples of n
- [[KL Divergence]] $P' || P$ measures how much optimization is done
	- As long as Continous , $$n - \frac{n-1}{n}$$

## Refs
- [openai](https://openai.com/blog/measuring-goodharts-law/)

## Backlinks

> - [Goodhart's Law](Goodhart's Law.md)
>   - [[Proxy Objective]]

_Backlinks last generated 2022-10-04 13:01:19_
