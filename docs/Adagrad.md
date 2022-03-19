## Adagrad
- Past squared grads as scaling factor for learning rate
- $$\begin{align}& g_n = \nabla_\theta L(\theta) \\ & r_n = r_{n-1} + g_n \odot g_n \\ & \Theta_{n+1} = \Theta_n - \alpha \frac{g_n}{\epsilon + \sqrt{r_n}} \end{align}$$
- $\odot$ is component wise multiply
- $\epsilon$ is for stability
<<<<<<< HEAD
- Doesnt forget past gradients



## Backlinks
* [[Optimization]]
	* [[Adagrad]]

## ...
=======
- Doesnt forget past gradients## Backlinks
* [[Optimizers]]
	* [[Adagrad]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
