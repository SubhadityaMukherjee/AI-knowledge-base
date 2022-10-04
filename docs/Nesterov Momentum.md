---
title: Nesterov Momentum

tags: optimizer gradients 
date modified: Thursday, August 11th 2022, 12:32:49 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Nesterov Momentum
- $$\begin{align}
&v_{t}= \gamma v_{t+1}+\eta \cdot \nabla_{\theta}J(\theta - \gamma v_{t-1}) \\
&\theta = \theta- v_{t}\\
\end{align}$$

## Backlinks

> - [Gradient Descent #gradients](Gradient Descent gradients.md)
>   - [[Nesterov Momentum]]

_Backlinks last generated 2022-10-04 13:01:19_
