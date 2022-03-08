# 0-1 Loss
- $\begin{cases} 1 & f(x)=y \\ 0 & f(x)\neq y\end{cases}$
- Classification

# Squared Error
- $(y- f(x))^2$
- Regression

# Absolute Error
- $\lvert y-f(x)\rvert$
- Penalize large errors

# Cross Entropy
- implicit distribution $p(Y|x;\theta)$ -> use CE
- $\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} log (p_{model}(Y|x))$
	- Categorical CE
		- Classification
		- $\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} \Sigma_{i=1}^C 1(y=i)log (p_{model}f_i(x|\theta))$
		- C is no of classes
	- MSE
		- Regression
		- $\mathscr{L}(\theta) = \frac{1}{2}\mathbb{E}_{(x,y) \sim P(X,Y)}||y-f(x;\theta)||^2$

# Log Likelihood Loss
- $L(U) = \Sigma_i log P(u_i| u_{i-k} ,…, u_{i-1} )$
- k is size of context window of past tokens