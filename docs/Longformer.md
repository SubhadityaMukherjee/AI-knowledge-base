---
title: Longformer

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Longformer
- [Longformer: the Long-Document Transformer](https://arxiv.org/abs/2004.05150)
- [[Transformer]]
- [[Sliding Window Attention]]
- [[Dilated Sliding Window Attention]]
- [[Global and Sliding Window Attention]]
- [[Attention|attention]] mechanism that scales linearly with sequence length
- drop-in replacement for the standard self-[[Attention|attention]]
- local windowed [[Attention|attention]] with a task motivated global [[Attention|attention]]
- text8
- enwik8
- consistently outperforms [[RoBERTa]] on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA
- Longformer-Encoder-Decoder (LED), a Longformer variant for supporting long document generative sequence-to-sequence tasks, and demonstrate its effectiveness on the arXiv summarization dataset

