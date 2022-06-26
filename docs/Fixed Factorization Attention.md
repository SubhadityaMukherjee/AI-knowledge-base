---
title: Fixed Factorization Attention

tags: architecture 
---

# Fixed Factorization Attention
- [paper](https://arxiv.org/abs/1904.10509v1)
- Specific cells summarize previous locations and propagate to all future cells.
- Part of [Sparse Transformer](Sparse%20Transformer.md)
- Fixed attention pattern with c = 1 limits expressivity
- many representations in the network are only used for one block whereas a small number of locations are used by all blocks.
- Choosing $c \in [8, 16, 32]$ for typical values of $l \in [128, 256]$ do well although this increases the computational cost of this method by $c$ in comparison to the [Strided Attention](Strided%20Attention.md)
- when using multiple heads, having them attend to distinct subblocks of length $c$ within the block of size $l$  was preferable to having them attend to the same subblock
- ![](assets/Pasted%20image%2020220621181149.png)
























