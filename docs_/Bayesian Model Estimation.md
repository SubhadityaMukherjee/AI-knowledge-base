# Bayesian Model Estimation
- Unlike frequentist, sometimes things like sample mean is not a good metric because it has a high variance. Might give different results with different trials in a real valued distribution
- The task is to estimate $\theta$ from the data
- [[Bayesian Prior]]
- Now there are two sources of info about the true distribution $p_{X}(\theta)$
	- The likelihood $p_{\otimes_{i}}x(D|\theta)$  of $\theta$ . Empirical data
	- Prior plausibility in $h(\theta)$
	- Since these are independant sources we can combine them by multiplication: $p_{\otimes_{i}}x(D|\theta)h(\theta)$ 
		- High values -> Candidate model $\theta$ is a good estimate
		- [[Bayesian Posterior]]
		- [[Posterior Mean estimate]]

## Advantages
- If priors are well chosen -> Better than frequentists with small sample sizes

## Disadvantages
- Computationally expensive

## Example
- ![[Pasted image 20220316120743.png]]
- ![[Pasted image 20220316120803.png]]
- Green : prior , Red: Posterior
- The posterior mean estimate is obtained by integrating $\int_{\mathbb{R}}\mu h(\mu|D)d\mu$
- Since this is different from sample mean -> Prior distribution really does influence the models

### [[Protein Modeling]]