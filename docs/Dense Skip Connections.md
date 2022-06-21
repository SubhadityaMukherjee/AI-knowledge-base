---
title: Dense Skip Connections
tag: architecture
---

# [[Dense]] Skip Connections
- $$x_i = F(x_0,x_1 ,… ,x_{i-1})$$
	- F : 3x3 [[conv]] + [[ReLU]] -> k feature maps
	- no of feature maps : $$k(i-1) + k_0$$ where k is growth rate (hyperparam)

- [[Skip Connection]]
















































