---
title: Fixed Factorization Attention

tags: architecture 
---

# Fixed Factorization [[Attention]]
- [paper](https://arxiv.org/abs/1904.10509v1)
- Specific cells summarize previous locations and propagate to all future cells.
- Part of [[Sparse Transformer]]
- Fixed [[Attention|attention]] pattern with c = 1 limits expressivity
- many representations in the network are only used for one block whereas a small number of locations are used by all blocks.
- Choosing $c \in [[Strided Attention|8, 16, 32]]
- when using multiple heads, having them attend to distinct subblocks of length $c$ within the block of size $l$  was preferable to having them attend to the same subblock
- ![[assets/Pasted image 20220621181149.png]]




















































## Backlinks

> - [Attention](Attention.md)
>   - [[Fixed Factorization Attention]]

_Backlinks last generated 2022-07-26 20:33:15_
