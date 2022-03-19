## Gradient Descent #gradients
- [[Backprop]]
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
<<<<<<< HEAD
		- $$\begin{align}& r_n = \gamma r_{n-1} + \alpha \nabla_\theta L(\theta - \gamma r_{n-1}) \\ & \Theta_{n+1} = \Theta_n -r_n \end{align}$$



## Backlinks
* [[Gradient Ascent]]
	* To maximize loss function unlike [[Gradient Descent gradients]]
	* Minimize distance between similar inputs [[Gradient Descent gradients]], maximize between dissimilar [[Gradient Ascent]]
* [[Contrastive Loss]]
	* Minimize distance between similar inputs [[Gradient Descent gradients]], maximize between dissimilar [[Gradient Ascent]]
* [[Optimization]]
=======
		- $$\begin{align}& r_n = \gamma r_{n-1} + \alpha \nabla_\theta L(\theta - \gamma r_{n-1}) \\ & \Theta_{n+1} = \Theta_n -r_n \end{align}$$## Backlinks
* [[Gradient Ascent]]
	* To maximize loss function unlike [[Gradient Descent gradients]]
* [[Contrastive Loss]]
	* Minimize distance between similar inputs [[Gradient Descent gradients]], maximize between dissimilar [[Gradient Ascent]]
* [[Optimizers]]
>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
	* [[Gradient Descent gradients]]
* [[Feature Learning]]
	* [[Gradient Descent gradients]] or [[LinearRegression]]

<<<<<<< HEAD
## ...
=======
>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9