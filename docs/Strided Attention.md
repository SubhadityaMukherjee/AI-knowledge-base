---
title: Strided Attention

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Strided]] [[Attention]]
- [paper](https://arxiv.org/abs/1904.10509v1)
- Sparse factorizations of the [[Attention|attention]] matrix
- Reduce to $O(n\sqrt{n})$
- Recompute [[Attention|attention]] matrices to save memory
- Fast [[Attention|attention]] kernels
- Works nicely for images, music etc with a periodic structure
- Otherwise with the [[Strided|strided]] pattern , the spatial coordinates do not correlate with the positions the elements might be more relevant in the future
- ![[assets/Pasted image 20220621175944.png]]

## Backlinks
> - [Sparse [[Transformer]]](Sparse Transformer.md)
>   - Uses [[Strided Attention]]
>
> - [Attention](Attention.md)
>   - [[Strided Attention]]

_Backlinks last generated 2022-10-04 13:01:19_