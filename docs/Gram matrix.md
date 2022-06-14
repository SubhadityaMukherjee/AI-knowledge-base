---
title: Gram matrix
tags: einsum
---

# Gram Matrix

```python
def gram_matrix_new(y):
    b, ch, h, w = y.shape
    return torch.einsum('bchw,bdhw->bcd', [y, y]) / (h * w)
```










