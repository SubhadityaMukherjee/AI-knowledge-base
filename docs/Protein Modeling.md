---
title: Protein Modeling
---

# Protein Modeling
- Using [[Bayesian]] models
- Task : Estimate [[probability]] mass function(because discrete) for a finite, discrete distribution -> given a histogram from a sample
- Large number of categories and small number of observations
- ![[Pasted image 20220316121901.png]]
	- Estimate [[probability]] distrib of amino acids in each column in a protein class. 20 dim [[pmf]] (one for each site)
	- Can be aligned
	- High chances of class not being present in data
		- [[MLE]] will assign 0 [[probability]] to X
		- Wrong decision made for a lot of them that were not in the training set
		- Cannot use

- 20 dim [[pmf]] for amnio acid distrib : $\theta = (\theta_{1}, … ,\theta_{20})' = (P(X=A), …, P(X=Y))'$
	- count vectors of amino acids found in a given site in training data D
	- Distributed according to [[Multinomial Distribution]] with l = 20

## Using Prior
- 0 probabilities should not occur. $$\mathcal{H} = (\theta_{1}, …, \theta_{20})' \in \mathbb{R}^{20}|\theta_{j} \in (0,1)$$ and $$ \Sigma_{j} \theta_{j}=1$$
	- 19 dim hypervolume
	- Continuous space and so can use [[pdf]]
	- [[Dirichlet Distribution]] is used to represent it because parameterized with l = 20
- ![[Pasted image 20220316123546.png]]
- $\alpha$s fixed beforehand


































