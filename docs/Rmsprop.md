---
title: Rmsprop
---

# Rmsprop
- RL
- More stable than [[Adagrad]]
- Moving exponential avg : older grads given less weight
- $$\begin{align} & r_n = \rho r_{n-1} + (1-\rho) g_n \odot g_n \\ &\Theta_{n+1} = \Theta_n - \alpha \frac{g_n}{\sqrt{\epsilon + r_n}} \end{align}$$ 
- $$\rho$$ is decay : 0.9, 0.99
























































