---
title: Block Sparse Kernel
tags: parallel
---

# Block Sparse Kernel
- For networks with block sparse weights
- Can choose amount of sparsity
- Can replace normal [[dense]] [[layers]] with sparse and wide or sparse and deep
- ![im](assets/Pasted%20Image%2020220425233755.png)
- Enables wider and deeper networks
- Only compute on non zero blocks
- ![im](assets/Pasted%20Image%2020220425233903.png)
- Connectivity is unaffected in the spatial dimensions
- Compute cost is only prop to number of non zero weights
- [[Small World graphs]]
- Also useful for compression

## Refs
- [openai](https://openai.com/blog/block-sparse-gpu-kernels/)


























































































