---
title: FastText
tags: einsum architecture
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




