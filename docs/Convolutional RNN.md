---
title: Convolutional RNN
tags: architecture
date modified: Thursday, August 11th 2022, 12:32:55 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Convolutional RNN
- $$h_t = \sigma_h(W_{hh}\star h_{t-1} + W_{xh}\star x_t + b_h)$$
- $$y_t = \sigma_y(W_{hy}\star h_t + b_y)$$
- $$\star$$ is spatial [[Conv]]
- 5D shapes -> [samples, timesteps, width, height, channels]
- Very memory intensive
- $$x^{2}+x$$

