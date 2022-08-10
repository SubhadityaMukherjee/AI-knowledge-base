---
tags: temp
title: Vanishing/exploding #gradients
date modified: Wednesday, August 10th 2022, 7:05:45 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Vanishing/exploding #gradients
- Ill conditioning - Something like a pit of despair
- $$\nabla_xE = W^T(g'(a)\circ \nabla_y E)$$
	- $$g' = 1-g^2$$
- Active neurons saturate -> prevent error #[Backprop](Backprop.md)
- $$g(a) \approx 1 \rightarrow \nabla_xE \approx 0$$
- W is initialized with random values << 1 -> gradient decays exponentially in each layer (max eigenvalue of weight matrix)
- Solutions
	- [Regularization](Regularization.md) , [Optimizers](Optimizers.md) , [Architectures](Architectures)

## …

