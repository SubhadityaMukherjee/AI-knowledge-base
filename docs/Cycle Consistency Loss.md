---
title: Cycle Consistency Loss

tags: generative loss
date modified: Sunday, December 11th 2022, 1:34:04 pm
date created: Sunday, December 11th 2022, 1:00:35 pm
---

# Cycle Consistency Loss
```toc
```

- For two domains X, Y mapping $G: X \rightarrow Y$, $F: Y \rightarrow X$
- trying to enforce the intuition that these mappings should be reverses of each other and that both mappings should be bijections
- Encourages $$F(G(x)) \approx x \text{ and } G(F(y)) \approx y$$
- reduces the space of possible mapping functions by enforcing forward and backwards consistency
- $$L_{cyc}(G,F) = \mathbb{E}_{x \sim p_{data}(x)}[||F(G(x))-x)||_{1}] + \mathbb{E}_{x \sim p_{data}(y)}[||G(F(x))-x)||_{1}]$$
- $$\mathcal{L}_{cyc}(G, F, X, Y) = \frac{1}{m}\Sigma_{i=1}^{m}[(F(G(x_{i})-x_{i})+ (G(F(y_{i}))-y_{i})]$$

## Backlinks

> - [CycleGAN](CycleGAN.md)
>   - $\mathcal{L}_{cyc}$ [[Cycle Consistency Loss]]
>   - Adversarial Loss + [[Cycle Consistency Loss]]

_Backlinks last generated 2023-01-28 14:37:47_