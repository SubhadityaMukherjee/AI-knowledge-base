---
title: LASER

tags: architecture 
---

# LASER
- [Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual Transfer and Beyond](https://arxiv.org/abs/1812.10464)
- joint multilingual sentence representations
- LASER
- Language-Agnostic SEntence Representations
- 93 languages, belonging to more than 30 different families and written in 28 different scripts
- universal language agnostic sentence embeddings
- train a single encoder to handle multiple languages, so that semantically similar sentences in different languages are close in the [embedding](Embedding.md) space
- single BiLSTM encoder with a shared BPE vocabulary for all languages
- coupled with an auxiliary decoder and trained on publicly available parallel corpora
- learn a classifier on top of the resulting embeddings using English annotated data only, and transfer it to any of the 93 languages without any modification
- [XNLI](XNLI)
- [MLDoc](MLDoc.md)
- [BUCC](BUCC.md)
- test set of aligned sentences in 112 languages






















