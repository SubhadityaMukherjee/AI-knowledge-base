---
title: Dot Product Attention

tags: architecture 
---

# Dot Product [[Attention]]
- [Luong et al., 2015](https://arxiv.org/pdf/1508.04025.pdf)
- $$f_{att}(h_{i}, s_{j}) = h_{i}^{T}s_{j}$$
- Equivalent to [[Multiplicative Attention]] with no trainable weight matrix. Performs better at larger dimensions
- Identity matrix
- $h$ is hidden state for encoder and $s$ is hidden state for decoder
- A type of [[Attention Alignment]]
- Final scores after [[Softmax]]
- ![[assets/Pasted image 20220621174933.png]]


























