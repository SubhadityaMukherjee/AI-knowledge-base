---
title: Soft Attention
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Soft [Attention](Attention.md)
- For a simple [Seq2Seq](Seq2Seq.md), all hidden state vectors $h_t$ across timesteps are linearly combined
- $$c_i = \Sigma_{j=1}^T \alpha_{ij} h_j$$
- $$a_{ij} = \frac{exp(e_{ij})}{\Sigma_{k=1}^T exp(e_{ij})}$$
- ![im](assets/Pasted%20image%2020220307181112.png)

