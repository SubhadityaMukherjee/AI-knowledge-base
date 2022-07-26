---
title: Vanishing/exploding #gradients
---

# Vanishing/exploding #gradients
- Ill conditioning - Something like a pit of despair
- $$\nabla_xE  = W^T(g'(a)\circ \nabla_y E)$$
	- $$g' = 1-g^2$$
- Active neurons saturate -> prevent error #[[Backprop]]
- $$g(a) \approx 1 \rightarrow \nabla_xE \approx 0$$
- W is initialized with random values << 1 -> gradient decays exponentially in each layer (max eigenvalue of weight matrix)
- Solutions
	- [[Regularization]] , [[Optimizers]] , [[Architectures]]
## …

























































































## Backlinks

> - [Swish](Swish.md)
>   - While Swish reportedly improves model performance (Ramachandran et al., 2017), it still does not allow you to avoid [[Vanishingexploding gradients]]
>    
> - [SRN](SRN.md)
>   - [[Vanishingexploding gradients]] , in [[Backprop]], they break down when sequences are long.
>    
> - [Skip Connection](Skip Connection.md)
>   - Transfer #gradients to prevent [[Vanishingexploding gradients]]
>    
> - [Issues](Issues.md)
>   - [[Vanishingexploding gradients]]

_Backlinks last generated 2022-07-26 20:33:15_
