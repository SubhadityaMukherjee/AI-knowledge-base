---
title: cross-layer parameter sharing

tags: architecture 
---

# Cross-layer Parameter Sharing
- between encoder segments, layer parameters are shared for every similar subsegment.
- This means that e.g. with 12 encoder segments:
	- The multi-head self-attention subsegments share parameters (i.e. weights) across all twelve layers.
	- The same is true for the feedforward segments.
- The consequence of this change is that the number of parameters is reduced significantly, simply because they are shared.
- the stabilization of the neural network due to parameter sharing. In other words, beyond simply reducing the computational cost involved with training, the paper suggests that sharing parameters can also improve the training process.
















