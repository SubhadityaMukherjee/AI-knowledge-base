---
title: Vanishing/exploding #gradients
---

# Vanishing/exploding #gradients
- Ill conditioning - Something like a pit of despair
- $$\nabla_xE  = W^T(g'(a)\circ \nabla_y E)$$
	- $$g' = 1-g^2$$
- Active neurons saturate -> prevent error #[[backprop]]
- $$g(a) \approx 1 \rightarrow \nabla_xE \approx 0$$
- W is initialized with random values << 1 -> gradient decays exponentially in each layer (max eigenvalue of weight matrix)
- Solutions
	- [[Regularization]] , [[Optimizers]] , [[Architectures]]
## …















