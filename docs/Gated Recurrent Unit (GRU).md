---
title: Gated Recurrent Unit (GRU)
tags: architecture
---

# Gated [Recurrent](Recurrent.md) Unit (GRU)
- ![Pasted image 20220621124840](assets/Pasted%20image%2020220621124840.png)
- Simplified [Long Short Term Memory (LSTM|[LSTM)](Long%20Short%20Term%20Memory%20(LSTM)]].md)
- It has an input and forget gate, no output gate
- Faster than LSTM in training, but does not perform well in many tasks
- Tries to forget what is not important

## The Math
- Two gates, [Sigmoid](Sigmoid.md)
	- Reset : $$g_r = \sigma(W_{hr}h_{t-1} + W_{xr}x_t + b_r)$$
	- Update :  $$g_u = \sigma(W_{hu}h_{t-1} + W_{xu}x_t + b_u)$$
- Hidden state proposal
	- $$\hat h_t = tanh(W_{xh}x_t + W_{hh}g_r\cdot h_{t-1} + b_h)$$
- Final hidden state
	- Linear [Interpolation](Interpolation.md) between last hidden state and proposal
	- $$h_t = (1-g_u)\cdot h_{t-1} + g_u \cdot \hat h_t$$






















































