---
title: cross-layer parameter sharing

tags: architecture 
---

# Cross-layer Parameter Sharing
- between encoder segments, layer parameters are shared for every similar subsegment.
- This means that e.g. with 12 encoder segments:
	- The multi-head self-[[Attention|attention]] subsegments share parameters (i.e. weights) across all twelve [[Layers|layers]].
	- The same is true for the feedforward segments.
- The consequence of this change is that the number of parameters is reduced significantly, simply because they are shared.
- the stabilization of the neural network due to parameter sharing. In other words, beyond simply reducing the computational cost involved with training, the paper suggests that sharing parameters can also improve the training process.






































## Backlinks

> - [ALBERT](ALBERT.md)
>   - [[cross-layer parameter sharing]]
>   - For [[cross-layer parameter sharing]], the authors looked at not performing cross-layer sharing, performing cross-layer sharing for the feedforward segments only, performing sharing for the [[Attention|attention]] segments, and performing sharing for all subsegments. It turns out that sharing the parameters for the [[Attention|attention]] segments is most effective, while sharing the feedforward segment parameters does not contribute significantly. This clearly illustrates the important role of the [[Attention|attention]] mechanism in [[Transformer]] models. Because, however, all-segment sharing significantly decreases the number of parameters, at only slightly worse performance compared to [[Attention|attention]]-only sharing, the authors to perform all-segment sharing instead.

_Backlinks last generated 2022-07-26 20:33:15_
