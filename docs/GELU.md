---
title: GELU
tags: architecture
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GELU
- [Paper](https://arxiv.org/abs/1606.08415v4)
- Smoother [[Relu]]
- $$x\Phi(x)$$ where $\Phi(x)$ is the [[Normal Distribution]] [[CDF]]
- Weights inputs by percentile, rather than by sign like [[Relu|ReLU]]
- $$GELU(x) = xP(X \leq x) = x\Phi(x) = x. \frac{1}{2}\left[ 1+erf\left( \frac{x}{\sqrt{ 2 }} \right) \right]$$
- If $X \sim \mathscr{N}(0,1)$
- Used in [[GPT3]], [[Transformer]], [[Vision Transformer]], [[BERT]]
- ![](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-05-27_at_12.48.44_PM.png)

## Backlinks
> - [ConvNeXt](ConvNeXt.md)
>   - [[GELU]] instead of [[Relu]] , a single activation for each block (the original [[Transformer]] module has just one activation after the MLP), fewer normalization [[Layers]], [[Batch Normalization]] substituted by [[Layer Normalization]] , and separate [[Downsampling|downsampling]] layer

_Backlinks last generated 2022-10-04 13:01:19_
