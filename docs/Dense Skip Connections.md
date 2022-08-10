---
tags: temp
title: Dense Skip Connections
tag: architecture
date modified: Wednesday, August 10th 2022, 11:41:30 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Dense](Dense.md) Skip Connections
- $$x_i = F(x_0,x_1 ,… ,x_{i-1})$$
	- F : 3x3 [Conv](Conv.md) + [Relu](Relu.md) -> k feature maps
	- no of feature maps : $$k(i-1) + k_0$$ where k is growth rate (hyperparam)
- [Skip Connection](Skip%20Connection.md)

