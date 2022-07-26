---
title: Probability
tags: index
---

# Probability
- [[Frequentist]]
- [[Bayesian]]


































































































## Backlinks

> - [Label Smoothing](Label Smoothing.md)
>   - [[Dense]] layer is generally the last one and combined with soft max leads to a [[Probability]] distribution
>   - Assume true label to be y, then a truth [[Probability]] distribution would be $p_i=1$  If i=y and 0 otherwise
>    
> - [[[Bayesian]] Neural Network](Bayesian Neural Network.md)
>   - Generally we want to learn Joint [[Probability]] distribution $P(y|x)$ but this does not use the model parameters w
>    
> - [Protein Modeling](Protein Modeling.md)
>   - Task : Estimate [[Probability]] mass function(because discrete) for a finite, discrete distribution -> given a histogram from a sample
>   - Estimate [[Probability]] distrib of amino acids in each column in a protein class. 20 dim [[PMF]] (one for each site)
>   - [[MLE]] will assign 0 [[Probability]] to X
>    
> - [[[Probability]] Density Function](PDF.md)
>   - # [[Probability]] Density Function
>    
> - [[[Bayesian]] Prior](Bayesian Prior.md)
>   - Use prior knowledge as beliefs (param vectors $\theta$). Cast in the form of a [[Probability]] distribution over the space $\Theta$ .
>    
> - [Rejection [[Sampling]]](Rejection Sampling.md)
>   - Take a point from g with [[Probability]] $f(\tilde x)/g_{0}(\tilde x)$
>   - Either accept or reject if satisfies [[Probability]]
>   - Drop a point from $g_{0}(x)$ with that [[Probability]]
>    
> - [Fundamentals](Fundamentals.md)
>   - [[Probability]]
>    
> - [Bayesian](Bayesian.md)
>   - [[Probability]] density function
>    
> - [Detailed Balance](Detailed Balance.md)
>   - If we pick some state x with the [[Probability]] given by g and multiply its prob g(x) with the transition [[Probability]] density T(x|y) (weighted by [[Probability]] density of x)  then its the same as the reverse weighted transiting [[Probability]] density from y to x
>   - If we pick some state x with the [[Probability]] given by g and multiply its prob g(x) with the transition [[Probability]] density T(x|y) (weighted by [[Probability]] density of x)  then its the same as the reverse weighted transiting [[Probability]] density from y to x
>   - If we pick some state x with the [[Probability]] given by g and multiply its prob g(x) with the transition [[Probability]] density T(x|y) (weighted by [[Probability]] density of x)  then its the same as the reverse weighted transiting [[Probability]] density from y to x
>   - If we pick some state x with the [[Probability]] given by g and multiply its prob g(x) with the transition [[Probability]] density T(x|y) (weighted by [[Probability]] density of x)  then its the same as the reverse weighted transiting [[Probability]] density from y to x
>    
> - [Binomial Distribution](Binomial Distribution.md)
>   - [[Bernoulli Distribution]] repeated for N independant trials with success [[Probability]] q
>    
> - [Cross [[Entropy]]](Cross Entropy.md)
>   - Cross-[[Entropy|entropy]] is a measure from the field of information theory, building upon [[Entropy|entropy]] and generally calculating the difference between two [[Probability]] [[distributions]].
>   - It is closely related to but is different from [[KL Divergence]] that calculates the relative [[Entropy|entropy]] between two [[Probability]] [[distributions]], whereas cross-[[Entropy|entropy]] can be thought to calculate the total [[Entropy|entropy]] between the [[Distributions.md|distributions]].
>    
> - [Decision Boundaries](Decision Boundaries.md)
>   - which yields the lowerst misclassification rate or highest [[Probability]] of correct classification
>   - [[Probability]] of obtaining a correct classification for $R_{i}$ is $$\Sigma_{i=1}^{k}P(X \in R_{i}, Y = c_{i})$$
>    
> - [Point Distribution](Point Distribution.md)
>   - [[Probability]] mass is concentrated in a few points
>    
> - [Proxy Objective](Proxy Objective.md)
>   - Suppose we have some sample space $S$ (such as the set of possible question-answer pairs), some [[Probability]] distribution $P$ over $S$, a true objective (or “reward”) $R_{true}: S \to \mathbb{R}$ , proxy objective $R_{proxy}:S \to \mathbb{R}$ and we optimize $R_{proxy}$ to get a new distribution $P'$
>    
> - [[[Bayesian]] Predictive Posterior](Bayesian Predictive Posterior.md)
>   - Computes predictions y with different model parameters w and weights them by the [[Probability]] of those params given an input x
>    
> - [Possion Distribution](Poisson Distribution.md)
>   - [[Probability]] that an event occurs k times within a given time interval
>    
> - [[[Probability]] Mass Function](PMF.md)
>   - # [[Probability]] Mass Function
>    
> - [Variational Autoencoder](VAE.md)
>   - Constraint loss function and a given [[Probability]] $\mathcal{D}$

_Backlinks last generated 2022-07-26 20:33:15_
