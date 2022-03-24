# Adagrad
- Past squared grads as scaling factor for learning rate
- $$\begin{align}& g_n = \nabla_\theta L(\theta) \\ & r_n = r_{n-1} + g_n \odot g_n \\ & \Theta_{n+1} = \Theta_n - \alpha \frac{g_n}{\epsilon + \sqrt{r_n}} \end{align}$$
- $\odot$ is component wise multiply
- $\epsilon$ is for stability
- Doesnt forget past gradients

## Backlinks
* [[Optimization]]
	* [[Adagrad]]

## …