---
title: Gated Recurrent Unit (GRU)
---

# Gated Recurrent Unit (GRU)
- Two gates, sigmoid
	- Reset : $$g_r = \sigma(W_{hr}h_{t-1} + W_{xr}x_t + b_r)$$
	- Update :  $$g_u = \sigma(W_{hu}h_{t-1} + W_{xu}x_t + b_u)$$
- Hidden state proposal
	- $$\hat h_t = tanh(W_{xh}x_t + W_{hh}g_r\cdot h_{t-1} + b_h)$$
- Final hidden state
	- Linear interpolation between last hidden state and proposal
	- $$h_t = (1-g_u)\cdot h_{t-1} + g_u \cdot \hat h_t$$





## Backlinks
* [[Basic RNN Architectures]]
	* [[Gated Recurrent Unit (GRU)]]

