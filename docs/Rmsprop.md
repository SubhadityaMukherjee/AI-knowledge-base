## Rmsprop
- RL
- More stable than Adagrad
- Moving exponential avg : older grads given less weight
- $$\begin{align} & r_n = \rho r_{n-1} + (1-\rho) g_n \odot g_n \\ &\Theta_{n+1} = \Theta_n - \alpha \frac{g_n}{\sqrt{\epsilon + r_n}} \end{align}$$ 
<<<<<<< HEAD
- $$\rho$$ is decay : 0.9, 0.99



## Backlinks
* [[Optimization]]
	* [[Rmsprop]]

## ...
=======
- $$\rho$$ is decay : 0.9, 0.99## Backlinks
* [[Optimizers]]
	* [[Rmsprop]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
