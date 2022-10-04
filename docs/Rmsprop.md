---
title: Rmsprop
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:46 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Rmsprop
- RL
- More stable than [[Adagrad]]
- Moving exponential avg : older grads given less weight
- $$\begin{align}\\
& E[g^{2}]_{t}= 0.9E[g^{2}]_{t-1}+ 0.1g^{2}_{t}\\
& \theta_{t+1}= \theta_{t}- \frac{\eta}{\sqrt{E[g^{2}])_{t}+\epsilon}}g_{t}
\end{align}
$$
- Suggested $\gamma=0.9$ and $\eta= 0.001$

## Backlinks

> - [Adam](Adam.md)
>   - [[Rmsprop]] + Momentum
>    
> - [Optimization](Optimizers.md)
>   - [[Rmsprop]]
>    
> - [Gradient Descent #gradients](Gradient Descent gradients.md)
>   - [[Rmsprop]]

_Backlinks last generated 2022-10-04 13:01:19_
