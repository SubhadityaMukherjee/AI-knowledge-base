---
title: Nesterov Momentum

tags: optimizer gradients 
date modified: Wednesday, August 10th 2022, 7:05:49 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Nesterov Momentum
- $$\begin{align}
&v_{t}= \gamma v_{t+1}+\eta \cdot \nabla_{\theta}J(\theta - \gamma v_{t-1}) \\
&\theta = \theta- v_{t}\\
\end{align}$$

