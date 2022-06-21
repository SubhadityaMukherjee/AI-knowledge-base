---
title: GLOW
tags: einsum architecture 
---

# GLOW

```python
def unsqueeze2d_new(input, factor=2):
    return rearrange(input, 'b (c h2 w2) h w -> b c (h h2) (w w2)', h2=factor, w2=factor)

def squeeze2d_new(input, factor=2):
    return rearrange(input, 'b c (h h2) (w w2) -> b (c h2 w2) h w', h2=factor, w2=factor)
```










































