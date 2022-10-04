---
title: Block Sparse Kernel
tags: parallel
date modified: Thursday, August 11th 2022, 12:32:56 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Block Sparse Kernel
- For networks with block sparse weights
- Can choose amount of sparsity
- Can replace normal [[Dense]] [[Layers]] with sparse and wide or sparse and deep
- ![[assets/Pasted image 20220425233755.png|im]]
- Enables wider and deeper networks
- Only compute on non zero blocks
- ![[assets/Pasted image 20220425233903.png|im]]
- Connectivity is unaffected in the spatial dimensions
- Compute cost is only prop to number of non zero weights
- [[Small World graphs]]
- Also useful for compression

## Refs
- [openai](https://openai.com/blog/block-sparse-gpu-kernels/)

## Backlinks

> - [SentimentAnalysis](SentimentAnalysis.md)
>   - [[Block Sparse Kernel]]
>    
> - [Optimizing Work](Optimizing Code.md)
>   - [[Block Sparse Kernel]]

_Backlinks last generated 2022-10-04 13:01:19_
