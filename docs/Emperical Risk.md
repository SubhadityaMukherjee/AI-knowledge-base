# Emperical Risk
- TRAINING ERROR. Mean loss computed over training examples
- $$R(f) = \mathbb{E} _{(X,Y) \sim P(X,Y)}[l(y, f(x))]$$
- $$R^{emp}(h) = \frac{1}{N}\Sigma_{i=1}^{N}L(h(x_{i}), y_{i})$$
- joint prob distribution $P(X\in A,Y=c)$$ is unknown
	- [[Decision Boundaries]]
	
- Learning set $$\mathcal L$$ is finite
- Need an estimator to evaluate it
	- Supervised Learning
		- Compute $$\mathcal L_{train}$$
		- Risk train = (1/M)(sum of loss values for (y, f(x)))
		- This is an unbiased estimator, so we can use it to approximate the optimal function f* that minimizes $$\mathbb{R}$$
		- This means that we find $$argmin_{f\in F} \hat R(f, \mathcal{L}_Train)$$ (out of all the possible functions)
		- $$lim_{M\rightarrow \infty}(f^*_{\mathcal{L}_Train}) = f^*$$ : converges to the fn that minimizes emprical risk
<<<<<<< HEAD
	- Ordinary least squares regression



## Backlinks
* [[Cross Validation]]
	* Get model with min [[Emperical Risk]]
* [[Fundamentals]]
	* [[Emperical Risk]]
* [[Bias Vs Variance]]
	* Tune on [[Emperical Risk]] instead using [[Optimizers]] 

## ...
=======
	- Ordinary least squares regression## Backlinks
* [[Cross Validation]]
	* Get model with min [[Emperical Risk]]
* [[Bias Variance Dilemma]]
	* Tune on [[Emperical Risk]] instead using [[Optimizers]] 
* [[Fundamentals]]
	* [[Emperical Risk]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
