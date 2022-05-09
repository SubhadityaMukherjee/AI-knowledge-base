---
title: Long Short Term Memory (LSTM)
tags: architecture
---

# Long Short Term Memory (LSTM)
- Smaller chance of exploding or vanishing #gradients
- Better ability to model long term dependencies
- Gated connections
- Splitting state into parts -> output pred and feature learning
- Gates
	- Forget $$g_f = \sigma(W_{hf}h_{t-1} + W_{xf}x_t + b_f)$$
		- How much of the previous cell state is used
	- Input $$g_i = \sigma(W_{hi}h_{t-1} + W_{xi}x_t + b_i)$$
		- How proposal is added to the state
	- Output $$g_o = \sigma(W_{ho}h_{t-1} + W_{xo}x_t + b_o)$$
		- Component wise products
- Hidden state
	- $$C_t$$ to model cross timestep dependencies
		- Cell state proposal : $$\hat C = tanh(W_{hc}h_{t-1} + W_{xc}x_t + b_c)$$
		- Final cell state : $$C_t = g_f \cdot C_{t-1} + g_i\cdot \hat C$$
	- $$h_t$$ to predict output
		- $$h_t = g_o \cdot \sigma_y(C_t)$$




































