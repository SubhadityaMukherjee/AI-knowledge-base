---
title: Block Sparse Kernel
tags: parallel
date modified: Wednesday, August 10th 2022, 11:41:31 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Block Sparse Kernel
- For networks with block sparse weights
- Can choose amount of sparsity
- Can replace normal [Dense](Dense.md) [Layers](Layers.md) with sparse and wide or sparse and deep
- ![im](assets/Pasted%20image%2020220425233755.png)
- Enables wider and deeper networks
- Only compute on non zero blocks
- ![im](assets/Pasted%20image%2020220425233903.png)
- Connectivity is unaffected in the spatial dimensions
- Compute cost is only prop to number of non zero weights
- [Small World graphs](Small%20World%20graphs.md)
- Also useful for compression

## Refs
- [openai](https://openai.com/blog/block-sparse-gpu-kernels/)

