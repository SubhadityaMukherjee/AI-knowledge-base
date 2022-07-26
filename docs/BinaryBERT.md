---
title: BinaryBERT

tags: architecture 
---

# BinaryBERT
- [BinaryBERT: Pushing the Limit of BERT Quantization](https://arxiv.org/abs/2012.15701)
- demand for model compression techniques
- weight binarization
- binary BERT is hard to be trained directly than a ternary counterpart due to its steep and complex loss landscape
- ternary weight splitting
- initializes BinaryBERT by equivalently splitting from a half-sized ternary network, followed by fine-tuning for further refinement
- binary model thus inherits the good performance of the ternary one, and can be further enhanced by fine-tuning the new architecture after splitting
- tailor the size of BinaryBERT based on the edge device constraints
- GLUE
- SQuAD
























