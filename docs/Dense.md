---
title: Dense
tag: architecture
---

# Dense
- Weighted [[LinearRegression]]
- Forward
	- $$z = W\cdot x + b$$ , $$y=g(z)$$
- Backward
	- $$\delta = g'(z)\circ \nabla_y E$$
	- $$\nabla_WE = \delta \cdot x^T$$ , $$\nabla_bE = \delta$$
	- $$\nabla_xE = W^T\cdot \delta$$




















