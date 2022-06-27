---
title: XLNet

tags: architecture 
---

# XLNet
- [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237)
- modeling bidirectional contexts
- denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling
- However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy
- generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order (thereby proposing a new objective called Permutation Language Modeling), and (2) overcomes the limitations of BERT thanks to its autoregressive formulation
- uses a permutation language modeling objective to combine the advantages of autoregressive and autoencoder methods




