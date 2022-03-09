# Optimization

## Gradient Descent #gradients
- [[Backprop]]
- Params $\theta$
- Minimize loss function $\mathscr{L}(\theta) = \Sigma^N_{n=1}l_n(\theta)$
	- First order
	- Normal update
		- proportional to negative grad of $\mathscr{L}$
		- $\theta_{t+1} = \theta{t} - \eta_t \Sigma_{n=1}^N(\nabla l_n(\theta_t))^T$
			- $\eta_t$ is learning rate
		- $\nabla$ is needed for all $l_n$ which is computationally expensive
		- Instead
			- Stochastic 
				- $\nabla l(\theta)$ for only one random sample. Repeat
				- lr : 0.01, 0.001
			- Mini Batch : $\nabla l(\theta)$ for a subset 
				- Possible because unbiased
				- Large variance
	- Momentum
		- $\begin{align} & r_n = \gamma r_{n-1} + \alpha \nabla_\theta L(\theta) \\& \Theta_{n+1} = \Theta_n -r_n\end{align}$
		- Common value of dampening factor $\gamma$ is 0.9
	- Nesterov Momentum
		- Look ahead by computing grads wrt future params
		- Better for rough landscapes
		- $\begin{align}& r_n = \gamma r_{n-1} + \alpha \nabla_\theta L(\theta - \gamma r_{n-1}) \\ & \Theta_{n+1} = \Theta_n -r_n \end{align}$

## Adagrad
- Past squared grads as scaling factor for learning rate
- $\begin{align}& g_n = \nabla_\theta L(\theta) \\ & r_n = r_{n-1} + g_n \odot g_n \\ & \Theta_{n+1} = \Theta_n - \alpha \frac{g_n}{\epsilon + \sqrt{r_n}} \end{align}$
- $\odot$ is component wise multiply
- $\epsilon$ is for stability
- Doesnt forget past gradients

## Rmsprop
- RL
- More stable than Adagrad
- Moving exponential avg : older grads given less weight
- $\begin{align} & r_n = \rho r_{n-1} + (1-\rho) g_n \odot g_n \\ &\Theta_{n+1} = \Theta_n - \alpha \frac{g_n}{\sqrt{\epsilon + r_n}} \end{align}$ 
- $\rho$ is decay : 0.9, 0.99

## Adam
- Supervised learning
- RMSProp + Momentum
- Corrects bias in exponentially weighted averages
- Struggles with large no of params -> Over smooths the gradient
- $\begin{align} & s_n = \rho_1 s_{n-1} + (1-\rho_1) g_n \\ & r_n = \rho_2 r_{n-1} + (1-\rho_2) g_n \odot g_n \\ & \Theta_{n+1} = \Theta_n - \alpha \frac{s_n}{\epsilon + \sqrt{r_n}} \frac{1-\rho_2^n}{1-\rho^n_1} \end{align}$
- First and second moments

## Learning Rate Decay #tricks
- Scale of loss landscape changes 
- Reduce step size near optima
- Factor $\alpha_{i+1} = d\cdot \alpha_i$
- LR Scheduling

## Early Stopping #tricks
- No of epochs is a hyper parameter : to prevent overfitting
