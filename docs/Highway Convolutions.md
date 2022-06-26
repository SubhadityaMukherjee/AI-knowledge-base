---
title: Highway Convolutions
tags: einsum architecture
---

# Highway Convolutions
- [[Conv]]

```python
class HighwayConv1dNew(nn.Conv1d):
    def forward(self, inputs):
        L = super().forward(inputs)
        H1, H2 = rearrange(L, 'b (split c) t -> split b c t', split=2)
        torch.sigmoid_(H1)
        return H1 * H2 + (1.0 - H1) * inputs
```




































































