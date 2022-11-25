---
title: Block Sparse Kernel
tags: parallel
date modified: Monday, October 10th 2022, 2:02:32 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Block Sparse Kernel
- For networks with block sparse weights
- Can choose amount of sparsity
- Can replace normal [Dense](Dense.md) [Layers](Layers.md) with sparse and wide or sparse and deep
- ![im](images/Pasted%20image%2020220425233755.png)
- Enables wider and deeper networks
- Only compute on non zero blocks
- ![im](images/Pasted%20image%2020220425233903.png)
- Connectivity is unaffected in the spatial dimensions
- Compute cost is only prop to number of non zero weights
- [Small_World_graphs](Small_World_graphs.md)
- Also useful for compression

## Refs
- [openai](https://openai.com/blog/block-sparse-gpu-kernels/)

