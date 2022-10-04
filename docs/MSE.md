---
title: MSE
tags: loss
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# MSE
- $$L(x) = \Sigma_i ||D(E(x_i))||^2$
- $$MSE = \frac{1}{N} \Sigma^N_{i=1}(p(x_i) - y_i)^2$$

## Backlinks

> - [Huber/Smooth L1/Smooth MAE](Huber.md)
>   - It is less sensitive to outliers than the [[MSE]] and in some cases prevents exploding #gradients
>    
> - [MSLE](MSLE.md)
>   - [[MSE]] log error
>    
> - [Log Cosh](LogCosh.md)
>   - works like the [[MSE]], but is smoothed towards large errors (presumably caused by outliers) so that the final error score isn’t impacted thoroughly.
>    
> - [Cross [[Entropy]]](Cross Entropy.md)
>   - [[MSE]]
>    
> - [AutoEncoder](Auto Encoders.md)
>   - [[MSE]] : Unsupervised

_Backlinks last generated 2022-10-04 13:01:19_
