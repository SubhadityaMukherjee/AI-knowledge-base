---
title: RoBERTa

tags: architecture 
---

# RoBERTa
- [RoBERTa: a Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)
- evaluates a number of design decisions when pretraining BERT models
- They find that BERT was significantly undertrained, and can match or exceed the performance of every model published after it.
- performance can be substantially improved by training the model longer, with bigger batches over more data; removing the next sentence prediction objective; training on longer sequences; and dynamically changing the masking pattern applied to the training data
- [[GLUE]]
- [[RACE]]
- [[SQuAD]]
- only the masked language model objective


























## Backlinks

> - [Longformer](Longformer.md)
>   - consistently outperforms [[RoBERTa]] on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA
>    
> - [BART](BART.md)
>   - matches the performance of [[RoBERTa]] with comparable training resource

_Backlinks last generated 2022-07-26 20:33:15_
