---
title: Strided Attention

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Strided](Strided.md) [Attention](Attention.md)
- [paper](https://arxiv.org/abs/1904.10509v1)
- Sparse factorizations of the [attention](Attention.md) matrix
- Reduce to $O(n\sqrt{n})$
- Recompute [attention](Attention.md) matrices to save memory
- Fast [attention](Attention.md) kernels
- Works nicely for images, music etc with a periodic structure
- Otherwise with the [strided](Strided.md) pattern , the spatial coordinates do not correlate with the positions the elements might be more relevant in the future
- ![Pasted image 20220621175944](assets/Pasted%20image%2020220621175944.png)

