---
title: Receptive field
tags: architecture 
---

# Receptive Field
- Not for Dense, only local connected [[Layers|layers]] like [[Conv]], [[Pooling]]
- A neuron's receptive field is the patch of the total field of view that a single neuron has access to
- Almost a logarithmic relationship between classification accuracy and receptive field size
	- Large fields are almost necessary for high level recognition tasks, but with diminishing rewards
- $$r(i-1) = s_{i}\times r_{i} + (k_{i}-s_{i})$$
- ![](https://theaisummer.com/static/f0e95de5fb54ce75ebdf93c0bd576ebe/77a9e/receptive-field-1d-conv-visualization.png)
- Recursive
	- $$r_{0} = \Sigma^{L}_{i=1}((k_{i}-1)\Pi_{j=1}^{l-1}s_{j})+1$$
- How to increase receptive field
	- Add more [[Conv]]
	- Add [[Pooling|pooling]] or higher stride
	- [[Causal Dilated Conv]]
	- [[Depthwise Separable]]










































## Backlinks

> - [Causal Dilated [[Conv]]](Causal Dilated Conv.md)
>   - [[Receptive field]] is how much of the input sequence is needed for one prediction

_Backlinks last generated 2022-07-26 20:33:15_
