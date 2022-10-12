---
title: Operator Fusion
tags: parallel
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Operator Fusion
- Some DirectML operators support a concept known as _fusion_. Operator fusion is a way to improve performance by merging one operator (typically, an activation function) into a different operator so that they are executed together without requiring a roundtrip to memory.
- <https://arxiv.org/abs/2108.13342>

## Backlinks
> - [Instant NeRF](Instant NeRF.md)
>   - fully-fused [[Operator Fusion]] CUDA kernels with a focus on minimizing wasted bandwidth and compute operations
>
> - [Optimizing Work](Optimizing Code.md)
>   - [[Operator Fusion]]

_Backlinks last generated 2022-10-04 13:01:19_
