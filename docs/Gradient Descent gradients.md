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
































































## Backlinks

> - [Learning Rate [[Scheduling]]](Learning Rate Scheduling.md)
>   - [[Gradient Descent gradients]]
>    
> - [Contrastive Loss](Contrastive Loss.md)
>   - Minimize distance between similar inputs [[Gradient Descent gradients]], maximize between dissimilar [[Gradient Ascent]]
>    
> - [Gradient Ascent](Gradient Ascent.md)
>   - To maximize loss function unlike [[Gradient Descent gradients]]
>    
> - [Optimization](Optimizers.md)
>   - [[Gradient Descent gradients]]
>    
> - [AutoEncoder](Auto Encoders.md)
>   - Learn using [[Gradient Descent gradients]]
>    
> - [GAN](Generative Models.md)
>   - G : [[Gradient Descent gradients]]
>    
> - [Methods for [Feature Learning](Feature%20Learning.md)](Methods for Feature Learning.md)
>   - [[Gradient Descent gradients]] or [[LinearRegression]]

_Backlinks last generated 2022-06-26 00:07:54_
