---
title: Soft Attention
tags: architecture 
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Soft [[Attention]]
- For a simple [[Seq2Seq]], all hidden state vectors $h_t$ across timesteps are linearly combined
- $$c_i = \Sigma_{j=1}^T \alpha_{ij} h_j$$
- $$a_{ij} = \frac{exp(e_{ij})}{\Sigma_{k=1}^T exp(e_{ij})}$$
- ![[assets/Pasted image 20220307181112.png|im]]

## Backlinks
> - [Scaled [[Dot Product Attention]]](Scaled Dot Product Attention.md)
>   - Generalization of [[Soft Attention]]
>
> - [Attention](Attention.md)
>   - [[Soft Attention]]

_Backlinks last generated 2022-10-04 13:01:19_
