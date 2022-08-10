---
title: RETRO

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# RETRO
- [Improving Language Models by Retrieving from Trillions of Tokens](https://arxiv.org/abs/2112.04426)
- Retrieval-Enhanced Transformer
- RETRO
- enhances auto-regressive language models by conditioning on document chunks retrieved from a large corpus
- based on local similarity with preceding tokens
- comparable performance to [GPT](GPT.md)-3 and Jurassic-1 on the Pile, despite using 25x fewer parameters
- frozen BERT retriever, a differentiable encoder and a chunked cross-[attention](Attention.md) mechanism to predict tokens based on an order of magnitude more data than what is typically consumed during training
- Wikitext103
- Pile
- improving semi-parametric language models through explicit memory can provide an orthogonal, more efficient approach than raw parameter scaling as they seek to build more powerful language models

