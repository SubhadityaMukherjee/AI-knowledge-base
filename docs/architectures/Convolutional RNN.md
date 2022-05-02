---
title: Convolutional RNN
---

# Convolutional RNN
- $$h_t = \sigma_h(W_{hh}\star h_{t-1} + W_{xh}\star x_t + b_h)$$
- $$y_t = \sigma_y(W_{hy}\star h_t + b_y)$$
- $$\star$$ is spatial [[conv]]
- 5D shapes -> [samples, timesteps, width, height, channels]
- Very memory intensive


