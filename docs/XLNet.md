---
title: XLNet

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# XLNet
- [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237)
- modeling bidirectional contexts
- denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling
- However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy
- generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order (thereby proposing a new objective called Permutation Language Modeling), and (2) overcomes the limitations of BERT thanks to its autoregressive formulation
- uses a permutation language modeling objective to combine the advantages of autoregressive and autoencoder methods

## Backlinks
> - [ELECTRA](ELECTRA.md)
>   - performs comparably to [[RoBERTa|[RoBERTa|[[RoBERTa]]](RoBERTa.md) and [[XLNet]] while using less than 1/4 of their compute and outperforms them when using the same amount of compute.

_Backlinks last generated 2022-10-04 13:01:19_
