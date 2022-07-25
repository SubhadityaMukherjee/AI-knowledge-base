---
title: GELU
tags: architecture
---

# GELU
- [Paper](https://arxiv.org/abs/1606.08415v4)
- Smoother [Relu](Relu.md)
- $$x\Phi(x)$$ where $\Phi(x)$ is the [Normal Distribution](Normal%20Distribution.md) [CDF](CDF.md)
- Weights inputs by percentile, rather than by sign like [ReLU](Relu.md)
- $$GELU(x) = xP(X \leq x) = x\Phi(x) = x. \frac{1}{2}\left[ 1+erf\left( \frac{x}{\sqrt{ 2 }} \right) \right]$$
- If $X \sim \mathscr{N}(0,1)$
- Used in [[GPT3]], [[Transformer]], [[Vision Transformer]], [[BERT]]
- ![](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-05-27_at_12.48.44_PM.png)




































