# Dropout
- Applied to Dense layers
- Training : Randomly (Bernoulli, p = 0.5 say) set #activations to 0
- Generally p = 0.1, 0.5
- Testing: Reweight by p
	- Because after training values will increase by $1/(1-p)$
- Reduces co dependence between neurons
- Decreases overfitting
- Start with small rate : 20 %

# Variational/Recurrent Dropout
- RNN
- Only on the non recurrent parts such as inputs and outputs
- In recorrent parts, use the same dropout mask for all time steps
- Same dropout mask for each time step
- ![[Pasted image 20220306113950.png]]

# Batch Normalization
- bias=False for Linear/Conv2D for input and True for output #tricks
- Normalizes #activations
- Input distributions change per layer -> Make sure they stay similar
- Reduces co variate shift because now the network must adapt per layer
- During testing : use stats saved during training
- Simplifies learning dynamics
	- Can use larger learning rate
	- Higher order interactions are suppressed because the mean and std are independant of the activations which makes training easier
- Cant work with small batches. Not great with RNN
- ![[Pasted image 20220306114903.png]]
- $\mu_j \leftarrow \frac{1}{m}\Sigma_{i=1}^m x_{ij}$
- $\sigma^2_j \leftarrow \frac{1}{m}\Sigma^m_{i=1}(x_{ij}-\mu_j)^2$
- $\hat x_{ij} \leftarrow \frac{x_{ij}-\mu_j}{\sqrt{\sigma^2_j + \epsilon}}$
- $\hat x_{ij} \leftarrow \gamma \hat x_{ij} + \beta$

# Layer Normalization
- For RNNs etc
- Mean and variance calculated independantly for each element of the batch by aggregating over the features dimensions.

[[Augmentation]]

# Lp Regularization
- Tikhonov
- Penalty considering weights
- $L^\ast(\theta) = L(\theta) + \lambda \Sigma_i |\theta_i|^p$
	- Lasso
		- p = 1
		- Sparse
		- With linear model : feature selection
	- Weight Decay
		- p = 2
		- Bayesian
		- Encourages optimization trajectory perpendicular to isocurves
		- ![[Pasted image 20220306133032.png]]
- Tune $\lambda$
	- Grid search : log scale
	- Too large : underfit, too small : overfit
	- Cross validation required