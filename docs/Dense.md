---
tags: temp
title: Dense
tag: architecture
date modified: Wednesday, August 10th 2022, 11:41:30 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Dense
- Weighted [LinearRegression](LinearRegression.md)
- Forward
	- $$z = W\cdot x + b$$ , $$y=g(z)$$
- Backward
	- $$\delta = g'(z)\circ \nabla_y E$$
	- $$\nabla_WE = \delta \cdot x^T$$ , $$\nabla_bE = \delta$$
	- $$\nabla_xE = W^T\cdot \delta$$

