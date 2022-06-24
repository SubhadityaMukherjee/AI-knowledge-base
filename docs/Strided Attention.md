---
title: Strided Attention

tags: architecture 
---

# [Strided](Strided.md) Attention
- [paper](https://arxiv.org/abs/1904.10509v1)
- Sparse factorizations of the attention matrix
- Reduce to $O(n\sqrt{n})$
- Recompute attention matrices to save memory
- Fast attention kernels
- Works nicely for images, music etc with a periodic structure
- Otherwise with the [strided](Strided.md) pattern , the spatial coordinates do not correlate with the positions the elements might be more relevant in the future
- ![](assets/Pasted%20image%2020220621175944.png)














