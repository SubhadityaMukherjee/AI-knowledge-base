---
title: Gradient Descent #gradients
---

# Gradient Descent #gradients
- [[Backprop]]
- Gradient Direction ~ Steepest Descent $$\theta = tan^{-1}(\frac{\frac{\partial f}{\partial y}}{\frac{\partial f}{\partial x}})$$
- Gradient Magnitude ~ Edge Strength $$||\triangledown f|| = \sqrt{(\frac{\partial f}{\partial x})^{2} + (\frac{\partial f}{\partial y})^{2}}$$
- Params $$\theta$$
- Minimize loss function $$\mathscr{L}(\theta) = \Sigma^N_{n=1}l_n(\theta)$$
	- First order
	- Normal update
		- proportional to negative grad of $$\mathscr{L}$$
		- $$\theta_{t+1} = \theta{t} - \eta_t \Sigma_{n=1}^N(\nabla l_n(\theta_t))^T$$
			- $$\eta_t$$ is learning rate
		- $$\nabla$$ is needed for all $$l_n$$ which is computationally expensive
		- Instead
			- Stochastic 
				- $$\nabla l(\theta)$$ for only one random sample. Repeat
				- lr : 0.01, 0.001
			- Mini Batch : $$\nabla l(\theta)$$ for a subset 
				- Possible because unbiased
				- Large variance
	- Momentum
		- $$\begin{align} & r_n = \gamma r_{n-1} + \alpha \nabla_\theta L(\theta) \\& \Theta_{n+1} = \Theta_n -r_n\end{align}$$
		- Common value of dampening factor $$\gamma$$ is 0.9
	- Nesterov Momentum
		- Look ahead by computing grads wrt future params
		- Better for rough landscapes
		- $$\begin{align}& r_n = \gamma r_{n-1} + \alpha \nabla_\theta L(\theta - \gamma r_{n-1}) \\ & \Theta_{n+1} = \Theta_n -r_n \end{align}$$

## …








































