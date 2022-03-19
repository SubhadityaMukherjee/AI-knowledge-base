## Cross Entropy
- implicit distribution $$p(Y|x;\theta)$$ -> use CE
- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} log (p_{model}(Y|x))$$
	- Categorical CE
		- Classification
		- $$\mathscr{L}(\theta) = -\mathbb{E}_{(x,y) \sim P(X,Y)} \Sigma_{i=1}^C 1(y=i)log (p_{model}f_i(x|\theta))$$
		- C is no of classes
	- MSE
		- Regression
		- $$\mathscr{L}(\theta) = \frac{1}{2}\mathbb{E}_{(x,y) \sim P(X,Y)}||y-f(x;\theta)||^2$$



## Backlinks
* [[KL Divergence]]
	* Entropy + [[Cross Entropy]]
* [[BCE with Logits]]
	* [[Cross Entropy]] + logits
	$$\\left(  - \\mathrm{sum}\\left( y \\cdot \\mathrm{logsoftmax}\\left( ŷ \\right) \\cdot weight \\right) \\right) \\cdot \\mathrm{//}\\left( 1, \\mathrm{size}\\left( y, 2 \\right) \\right)$$
* [[Loss Functions]]
	* [[Cross Entropy]]

## ...