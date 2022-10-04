---
title: Multiplicative Attention

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:49 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Multiplicative [[Attention]]
- ![[assets/Pasted image 20220621174943.png]]
- $$f_{att}(h_{i}, s_{j}) = h_{i}^{T}W_{a}s_{j}$$
- Since [[Additive Attention]] performs better for scale, use a factor [[Scaled Dot Product Attention]]

## Backlinks

> - [Dot Product [[Attention]]](Dot Product Attention.md)
>   - Equivalent to [[Multiplicative Attention]] with no trainable weight matrix. Performs better at larger dimensions

_Backlinks last generated 2022-10-04 13:01:19_
