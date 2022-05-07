---
title: Central Limit Theorem
---

# Central Limit Theorem
- When random effects of many independant small sized causes sum up to large scale observable effects : one gets the [[normal distribution]]
- Let $(X_{i})_{i\in N}$ is a seq of independant, real valued, [[Square Integrable]] random variable with non zero variances $Var(X_{i}) = E[(X_{i}- E[X_{i}])^{2}]$ . Then If the [[distributions]] $P_{S_{n}}$ of standardized sum variables converge weakly to $\mathscr{N}(0,1)$ . $$S_{n}= \frac{\Sigma_{i= 1}^{n}(X_{i}- E[X_{i}])}{\sigma(\Sigma^{n}_{i=1}X_{i})}$$
	- Converge weakly : $$lim_{n\rightarrow\infty}\int f(x)P_{n}(dx) = \int f(x)P(dx)$$ for all $f: \mathbb{R} \rightarrow \mathbb{R}$
	- Lebesgue Integrals

## $X_{i}$ Are Identically Distributed
- Regardless of shape of each $X_{i}$, distribution of normalized sum converges to $\mathscr{N}(0,1)$ 
- Uniformly bounded
- None of the $X_{i}$ dominates the other "washing out"
























