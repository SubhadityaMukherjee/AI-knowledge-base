---
tags: temp
title: Dense Skip Connections
tag: architecture
date modified: Thursday, August 11th 2022, 12:32:55 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Dense]] Skip Connections
- $$x_i = F(x_0,x_1 ,… ,x_{i-1})$$
	- F : 3x3 [[Conv]] + [[Relu]] -> k feature maps
	- no of feature maps : $$k(i-1) + k_0$$ where k is growth rate (hyperparam)
- [[Skip Connection]]

