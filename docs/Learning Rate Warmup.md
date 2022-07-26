---
title: Learning Rate Warmup
---

# Learning Rate Warmup
- Small learning rate at the start and then a larger learning rate when the training is stabilized
- Linearly from 0 to initial rate
- First m batches to warm up and if the initial learning rate is $\eta$ then at batch i, $1 \leq i \leq m$ , learning rate is $$\frac{i\eta}{m}$$


































































































## Backlinks

> - [Learning Rate [[Scheduling]]](Learning Rate Scheduling.md)
>   - [[Learning Rate Warmup]]
>    
> - [Cosine Learning Rate Decay](Cosine Learning Rate Decay.md)
>   - Instead of [[Learning Rate Warmup]] and then decay

_Backlinks last generated 2022-07-26 20:33:15_
