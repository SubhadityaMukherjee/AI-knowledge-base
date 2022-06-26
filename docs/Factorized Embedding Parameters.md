---
title: Factorized Embedding Parameters

tags: architecture 
---

# Factorized Embedding Parameters
- Factorization of these parameters is achieved by taking the matrix representing the weights of the word embeddings $E$ and decomposing it into two different matrices. Instead of projecting the one-hot encoded vectors directly onto the hidden space, they are first projected on some-kind of lower-dimensional embedding space, which is then projected to the hidden space (Lan et al, 2019). Normally, this should not produce a different result, but let's wait.
- Another thing that actually ensures that this change reduces the number of parameters is that the authors suggest to reduce the size of the embedding matrix.
- In [BERT](BERT.md), the shape of the vocabulary/embedding matrix E equals that of the matrix for the hidden state H.
- First of all, theoretically, the matrix E captures context-independent information
- whereas the hidden representation H captures context-dependent information
- [ALBERT](ALBERT.md) solves this issue by decomposing the embedding parameters into two smaller matrices, allowing a two-step mapping between the original [word vectors](Word%20Vectors.md) and the space of the hidden state. In terms of computational cost, this no longer means $\text{O(VxH)}$ but rather $\text{O(VxE + ExH)}$, which brings a significant reduction when $\text{H >> E}$.












