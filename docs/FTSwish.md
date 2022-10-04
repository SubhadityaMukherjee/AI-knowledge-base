---
title: FTSwish

tags: activations 
date modified: Thursday, August 11th 2022, 12:32:54 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FTSwish
- ![[assets/Pasted image 20220626150952.png]]
- [[Relu]] + [[Sigmoid]]
- $$\begin{equation} FTSwish: f(x) = \begin{cases} T, & \text{if}\ x < 0 \\ \frac{x}{1 + e^{-x}} + T, & \text{otherwise} \\ \end{cases} \end{equation}$$
- As we can see, the sparsity principle is still true - the neurons that produce negative values are taken out.
- What we also see is that the derivative of FTSwish is smooth, which is what made [[Swish]] theoretically better than [[Relu|ReLU]] in terms of the loss landscape
- However, what I must note is that this function does not protect us from the dying [[Relu|ReLU]] problem: the gradients for $x < 0$ are zero, as with [[Relu|ReLU]].

