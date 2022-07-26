---
title: Inception
tags: architecture
---

# Inception
- [Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842)
- [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)

### V1
- [[Conv]] at different filter scales to find different kinds of [[Features|features]] -> stack them up
- Increasing both the depth and width of the network while keeping computations at a manageable level
- Human visual system wherein information is processed at multiple scales and then aggregated locally
- channel [[Dimensionality Reduction|dimensionality reduction]], by reducing the output channels of the input
- To enable concatenation of [[Features|features]] convolved with different kernels, they pad the output to make it the same size as the input.
	- without dilation
	- padding $p = (k-1)/2p$
	- since $out = in +2p -k +1$
- ![[assets/Pasted image 20220306120214.png|im]]

### V2/V3
- nxn [[Conv]] -> 1xn followed by nx1 [[Conv]]
- 5x5, 7x7 -> 2 and three 3x3 seq [[Conv]]
- More filters (wider)
- Distributed the computational budget in a balanced way between the depth and width of the network
- Added [[Batch Normalization]]
- ![[assets/Pasted image 20220306121513.png|im]]






























































































