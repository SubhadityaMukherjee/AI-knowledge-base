---
title: FastText
tags: einsum architecture
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FastText
```python
def FastTextNew(vocab_size, embedding_dim, output_dim):
    return nn.Sequential(
        Rearrange('t b -> t b'),
        nn.Embedding(vocab_size, embedding_dim),
        Reduce('t b c -> b c', 'mean'),
        nn.Linear(embedding_dim, output_dim),
        Rearrange('b c -> b c'),
    )
```

