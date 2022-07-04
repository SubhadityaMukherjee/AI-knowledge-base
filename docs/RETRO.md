---
title: RETRO

tags: architecture 
---

# RETRO
- [Improving Language Models by Retrieving from Trillions of Tokens](https://arxiv.org/abs/2112.04426)
- Retrieval-Enhanced Transformer
- RETRO
- enhances auto-regressive language models by conditioning on document chunks retrieved from a large corpus
- based on local similarity with preceding tokens
- comparable performance to GPT-3 and Jurassic-1 on the Pile, despite using 25x fewer parameters
- frozen BERT retriever, a differentiable encoder and a chunked cross-attention mechanism to predict tokens based on an order of magnitude more data than what is typically consumed during training
- Wikitext103
- Pile
- improving semi-parametric language models through explicit memory can provide an orthogonal, more efficient approach than raw parameter scaling as they seek to build more powerful language models






