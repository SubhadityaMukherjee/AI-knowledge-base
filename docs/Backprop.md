---
title: Backprop
---

# Backprop
- Gradient $$\nabla l(\theta) = [\frac{\partial l}{\partial \theta_1}(\theta) , … , \frac{\partial L}{\partial \theta_L}(\theta)]$$
	- partial derivs of the loss wrt weights
	 Forward pass
		- ![[Pasted image 20220304123536.png]]
		- Store result of operation in u
	- Backward Pass
		- ![[Pasted image 20220304123626.png]]
		- Traverse the graph backwards
			- Chain Rule : $$\frac{dl}{d\theta_i} = \Sigma_{k \in parents(l)} \frac{\partial l}{\partial u_k} \frac{\partial u_k}{\partial \theta_i}$$
			- $$\begin{align} &\frac{d\hat y}{d\mathbf{W_1}}\\ &= \frac{\partial \hat y}{\partial u_2} \frac{\partial u_2}{\partial h_1} \frac{\partial h_1}{\partial u_1} \frac{\partial u_1}{\partial \mathbf{W_1}} \\ &= \frac{\partial \sigma (u2)}{\partial u_2} \frac{\partial \mathbf{W}^T_2 h_1}{\partial h_1} \frac{\partial \sigma (u1)}{\partial u_1} \frac{\partial \mathbf{W}^T_1 x}{\partial \mathbf{W}_1} \end{align}$$
			- Collecting all the $$\partial \sigma(u_i)$$ wrt params -> #gradients exponentially decreases wrt depth of the network : Vanishing
				- Solved by [[ActivationFunctions]]






















