---
title: Transformer
tags: architecture
---

# Transformer
- Encoder Decoder
- Auto regressive : decoder outputs fed back as inputs to decoder
- Decoder can access not only the hidden step of the last time step from the encoder, but all the hidden states from the encoder
- During decoding, consider pairwise relationshop between decoder state and all the returned states from the encoder
	- Some words relevant, others are not
- Transform all hidden states from the encoder into context vectors, that shows how the decoding step is relevant to the input sequences
- [[Attention]]
- [[Basic Transformer]]

## Nice Little Blogs
- [lillog](https://lilianweng.github.io/posts/2018-06-24-attention/)












