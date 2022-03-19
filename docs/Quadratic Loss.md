# Quadratic Loss
- $$W = argmin_{W^{\ast}}\Sigma^N_{i=1} ||W^{\ast} x_i - y_i||^2$$
- $$\Delta : \mathbb{R}^{n} \rightarrow \mathbb{R}, x \rightarrow E[Y|X = x]$$ is the gold standard for minimizing this. But $\Delta$ is unknown## Backlinks
* [[LinearRegression]]
	* [[Quadratic Loss]]
* [[Window Based Regression]]
	* Flatten into $$d \\cdot k$$ vector and apply [[Quadratic Loss]]
* [[LossFunctions]]
	* [[Quadratic Loss]]
* [[Bias Variance Dilemma]]
	* [[Quadratic Loss]] (risk) is minimized by the function $$\\Delta(x) = E\_{Y|X=x}[Y]$$

