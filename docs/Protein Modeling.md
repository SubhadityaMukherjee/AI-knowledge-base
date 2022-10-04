---
tags: temp
title: Protein Modeling
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Protein Modeling
- Using [[Bayesian]] models
- Task : Estimate [[Probability]] mass function(because discrete) for a finite, discrete distribution -> given a histogram from a sample
- Large number of categories and small number of observations
- ![[assets/Pasted image 20220316121901.png|im]]
	- Estimate [[Probability]] distrib of amino acids in each column in a protein class. 20 dim [[PMF]] (one for each site)
	- Can be aligned
	- High chances of class not being present in data
		- [[MLE]] will assign 0 [[Probability]] to X
		- Wrong decision made for a lot of them that were not in the training set
		- Cannot use
- 20 dim [[PMF]] for amnio acid distrib : $\theta = (\theta_{1}, … ,\theta_{20})' = (P(X=A), …, P(X=Y))'$
	- count vectors of amino acids found in a given site in training data D
	- Distributed according to [[Multinomial Distribution]] with l = 20

## Using Prior
- 0 probabilities should not occur. $$\mathcal{H} = (\theta_{1}, …, \theta_{20})' \in \mathbb{R}^{20}|\theta_{j} \in (0,1)$$ and $$ \Sigma_{j} \theta_{j}=1$$
	- 19 dim hypervolume
	- Continuous space and so can use [[PDF]]
	- [[Dirichlet Distribution]] is used to represent it because parameterized with l = 20
- ![[assets/Pasted image 20220316123546.png|im]]
- $\alpha$s fixed beforehand

## Backlinks

> - [[[Bayesian]] Model Estimation](Bayesian Model Estimation.md)
>   - ### [[Protein Modeling]]

_Backlinks last generated 2022-10-04 13:01:19_
