---
title: Instance Normalization

tags: architecture 
date modified: Sunday, December 11th 2022, 1:16:14 pm
date created: Sunday, December 11th 2022, 1:15:01 pm
---

# Instance Normalization
```toc
```
- Contrast Normalization
- $$
    y_{tijk} = \frac{x_{tijk} - \mu_{ti}}{\sqrt{\sigma_{ti}^2 + \epsilon}},
    \quad
    \mu_{ti} = \frac{1}{HW}\sum_{l=1}^W \sum_{m=1}^H x_{tilm},
    \quad
    \sigma_{ti}^2 = \frac{1}{HW}\sum_{l=1}^W \sum_{m=1}^H (x_{tilm} - mu_{ti})^2
$$
- This prevents instance-specific mean and covariance shift simplifying the learning process.
- Intuitively, the normalization process allows to remove instance-specific contrast information from the content image in a task like image stylization, which simplifies generation.
- ![[Pasted image 20221211131622.png]]

## Backlinks

> - [AdaIn](AdaIn.md)
>   - Adaptive [[Instance Normalization]] is a normalization method that aligns the mean and variance of the content [features](Features.md) with those of the style [features](Features.md).
>    
> - [CycleGAN](CycleGAN.md)
>   - [[Instance Normalization]]

_Backlinks last generated 2023-01-28 14:37:47_
