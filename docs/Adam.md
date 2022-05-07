---
title: Adam
---

# Adam
- Supervised learning
- [[RMSProp]] + Momentum
- Corrects bias in exponentially weighted averages
- Struggles with large no of params -> Over smooths the gradient
- $$\begin{align} & s_n = \rho_1 s_{n-1} + (1-\rho_1) g_n \\ & r_n = \rho_2 r_{n-1} + (1-\rho_2) g_n \odot g_n \\ & \Theta_{n+1} = \Theta_n - \alpha \frac{s_n}{\epsilon + \sqrt{r_n}} \frac{1-\rho_2^n}{1-\rho^n_1} \end{align}$$
- First and second moments


























