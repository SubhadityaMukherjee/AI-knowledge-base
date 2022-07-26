---
title: Factorized Embedding Parameters

tags: architecture 
---

# Factorized [[Embedding]] Parameters
- Factorization of these parameters is achieved by taking the matrix representing the weights of the word embeddings $E$ and decomposing it into two different matrices. Instead of projecting the one-hot encoded vectors directly onto the hidden space, they are first projected on some-kind of lower-dimensional [[Embedding|embedding]] space, which is then projected to the hidden space (Lan et al, 2019). Normally, this should not produce a different result, but let's wait.
- Another thing that actually ensures that this change reduces the number of parameters is that the authors suggest to reduce the size of the [[Embedding|embedding]] matrix.
- In [[BERT]], the shape of the vocabulary/[[Embedding|embedding]] matrix E equals that of the matrix for the hidden state H.
- First of all, theoretically, the matrix E captures context-independent information
- whereas the hidden representation H captures context-dependent information
- [[ALBERT]] solves this issue by decomposing the [[Embedding|embedding]] parameters into two smaller matrices, allowing a two-step mapping between the original [[Word Vectors|word vectors]] and the space of the hidden state. In terms of computational cost, this no longer means $\text{O(VxH)}$ but rather $\text{O(VxE + ExH)}$, which brings a significant reduction when $\text{H >> E}$.






































## Backlinks

> - [ALBERT](ALBERT.md)
>   - [[Factorized Embedding Parameters]]
>   - For [[Factorized Embedding Parameters]], the authors report good performance. Both the case where cross-layer parameters were not shared and where they were, are reported. Without sharing, larger [[Embedding|embedding]] sizes give better performance. With sharing, performance boosts satisfy at an [[Embedding|embedding]] size of 128 dimensions. That's why the 128-size embeddings were used in the table above.

_Backlinks last generated 2022-07-26 20:33:15_
