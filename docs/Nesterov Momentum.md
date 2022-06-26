---
title: Nesterov Momentum

tags: optimizer gradients 
---

# Nesterov Momentum
- $$\begin{align}
&v_{t}= \gamma v_{t+1}+\eta \cdot \nabla_{\theta}J(\theta - \gamma v_{t-1}) \\
&\theta = \theta- v_{t}\\
\end{align}$$


## Backlinks

> - [Gradient Descent #gradients](Gradient Descent gradients.md)
>   - [[Nesterov Momentum]]

_Backlinks last generated 2022-06-26 12:48:16_
