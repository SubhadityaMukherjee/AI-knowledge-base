# Probability Density Function
- If X is a random variable(RV) that takes values in $S \subseteq \mathbb{R}^{n}$. PDF is a fn $f:S \rightarrow \mathbb{R}^{\geq0}$ that satisfies:
	- For every subvolume $A \subseteq S$ of S, the prob $P(X \in A)$ that X gives a value in A is $$P(X\in A) = \int_Af(x)dx$$## Backlinks
* [[Exponential Distribution]]
	* [[PDF]] $$p(x) = \\lambda e^{-\\lambda x}$$ and $x \\geq 0$
* [[Dirichlet Distribution]]
	* [[PDF]]
* [[N-dim Normal]]
	* [[PDF]] $$p(x) = \\frac{1}{(2\\pi)^{n/2}det(\\Sigma)^{\\frac{1}{2}}}exp\\left(-\\frac{1}{2}(x-\\mu)'\\Sigma^{-1}(x-\\mu)\\right)$$
* [[Point Distribution]]
	* [[PDF]] is impossible to use
* [[Uniform Distribution]]
	* [[PDF]] $$p(x) = \\begin{cases}\\frac{1}{(b*{1}-a*{1})\\cdot…\\cdot(b*{n}, a*{n})} & \\text{if } x \\in I\\[2ex]0&\\text{if x }\\notin I \\end{cases}$$

