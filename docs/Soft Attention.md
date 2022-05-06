---
title: Soft Attention
---

# Soft Attention
- For a simple Seq2Seq, all hidden state vectors $h_t$ across timesteps are linearly combined
- $$c_i = \Sigma_{j=1}^T \alpha_{ij} h_j$$
- $$a_{ij} = \frac{exp(e_{ij})}{\Sigma_{k=1}^T exp(e_{ij})}$$
- ![[Pasted image 20220307181112.png]]














