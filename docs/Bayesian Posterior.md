---
title: Bayesian Posterior
---

# [[Bayesian]] Posterior
- When D is fixed though, this becomes a function of Model Candidates
- Non negative on K dim param space
- Not a [[PDF]] but if we divide it by its integral -> [[PDF]] . 
	- $$\frac{p_{\otimes_{i}}x(D|\theta)h(\theta)}{\int_{\mathbb{R}^K}p_{\otimes_{i}}x(D|\theta)h(\theta)d\theta}$$
	- Prob distrib over candidate models
- If the denominator is replaced written as $p(D)$ then it looks like the [[Bayes Rule]]
- Shape : $P(D|\theta)h(\theta)$ 
	- Integral not 1
	- [[Proto Distributions]] on $\theta$ space


































































































## Backlinks

> - [[[Bayesian]] Model Estimation](Bayesian Model Estimation.md)
>   - [[Bayesian Posterior]]
>   - How to encode or represent [[Bayesian Posterior]] as very high dim
>    
> - [Inductive Bias](Inductive Bias.md)
>   - [[Bayesian Prior]] can shape the [[Bayesian Posterior]] in the way that it can be a similar distribution to the former
>    
> - [[[Bayesian]] Predictive Posterior](Bayesian Predictive Posterior.md)
>   - Follows from [[Bayesian Posterior]]

_Backlinks last generated 2022-07-26 20:33:15_
