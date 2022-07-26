---
title: Soft Attention
tags: architecture 
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

_Backlinks last generated 2022-07-26 20:33:15_
