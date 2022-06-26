---
title: ConvBERT

tags: architecture 
---

# ConvBERT
- Convolutional BERT (ConvBERT) improves the original [BERT](BERT.md) by replacing some [Multi Head Attention](Multi%20Head%20Attention.md) [Self Attention](Self%20Attention.md) segments with cheaper and naturally local operations, so-called [[span-based dynamic convolutions]]. These are integrated into the self-attention mechanism to form a mixed attention mechanism, allowing Multi-headed Self-attention to capture global patterns; the Convolutions focus more on the local patterns, which are otherwise captured anyway. In other words, they reduce the computational intensity of training BERT.


