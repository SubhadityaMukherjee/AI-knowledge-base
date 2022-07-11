---
title: SGD

tags: optimizer gradients 
---

# SGD
- instead of taking the whole dataset for each iteration, we randomly select the batches of data
- The procedure is first to select the initial parameters w and learning rate n. Then randomly shuffle the data at each iteration to reach an approximate minimum.
- full of noise
- Due to an increase in the number of iterations, the overall computation time increases.
- $$\theta = \theta - \eta \cdot \nabla_{\theta} J(\theta ; x^{i}; y^{i} )$$
	- For each example $x^{i}$ and label $y^{i}$


























