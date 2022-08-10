---
title: He Initialization

tags: regularize
date modified: Wednesday, August 10th 2022, 7:05:52 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# He Initialization
- bring the variance of those outputs to approximately one
- However, Kumar indeed proves mathematically that for the ReLU activation function, the best weight initialization strategy is to initialize the weights randomly but with this variance:
	- $$\begin{equation} v^{2} = 2/N \end{equation}$$
- For Sigmoid based activation functions

