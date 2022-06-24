---
title: Receptive field
tags: architecture 
---

# Receptive Field
- Not for Dense, only local connected layers like [[Conv]], [Pooling](Pooling.md)
- A neuron's receptive field is the patch of the total field of view that a single neuron has access to
- Almost a logarithmic relationship between classification accuracy and receptive field size
	- Large fields are almost necessary for high level recognition tasks, but with diminishing rewards
- $$r(i-1) = s_{i}\times r_{i} + (k_{i}-s_{i})$$
- ![](https://theaisummer.com/static/f0e95de5fb54ce75ebdf93c0bd576ebe/77a9e/receptive-field-1d-conv-visualization.png)
- Recursive
	- $$r_{0} = \Sigma^{L}_{i=1}((k_{i}-1)\Pi_{j=1}^{l-1}s_{j})+1$$
- How to increase receptive field
	- Add more [[Conv]]
	- Add [pooling](Pooling.md) or higher stride
	- [Causal Dilated Conv](Causal%20Dilated%20Conv.md)
	- [Depthwise Separable](Depthwise%20Separable.md)


