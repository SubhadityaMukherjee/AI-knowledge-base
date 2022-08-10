---
title: MobileOne

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# MobileOne
- [An Improved One Millisecond Mobile Backbone](https://arxiv.org/abs/2206.04040)
- extensive analysis of different metrics by deploying several mobile friendly networks on a mobile device
- identify and analyze architectural and optimization bottlenecks
- many times faster on mobile
- Inspired by[RepVGG](RepVGG.md)
- Either [ReLU](Relu.md) or SE-[ReLU](Relu.md) is used as activation. The trivial over-parameterization factor $k$ is a hyperparameter which is tuned for every variant.
- better top-1 accuracy on [ImageNet](ImageNet.md) than [EfficientNet](EfficientNet.md) at similar latency
- ![Pasted image 20220620164552](assets/Pasted%20image%2020220620164552.jpg)

