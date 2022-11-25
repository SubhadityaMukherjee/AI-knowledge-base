---
title: Longformer

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Longformer
- [Longformer: the Long-Document Transformer](https://arxiv.org/abs/2004.05150)
- [Transformer](Transformer.md)
- [Sliding_Window_Attention](Sliding_Window_Attention.md)
- [Dilated_Sliding_Window_Attention](Dilated_Sliding_Window_Attention.md)
- [Global_and_Sliding_Window_Attention](Global_and_Sliding_Window_Attention.md)
- [attention](Attention.md) mechanism that scales linearly with sequence length
- drop-in replacement for the standard self-[attention](Attention.md)
- local windowed [attention](Attention.md) with a task motivated global [attention](Attention.md)
- text8
- enwik8
- consistently outperforms [RoBERTa](RoBERTa.md) on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA
- Longformer-Encoder-Decoder (LED), a Longformer variant for supporting long document generative sequence-to-sequence tasks, and demonstrate its effectiveness on the arXiv summarization dataset

