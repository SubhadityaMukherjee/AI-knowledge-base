---
title: GLOW
tags: einsum architecture 
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GLOW
```python
def unsqueeze2d_new(input, factor=2):
    return rearrange(input, 'b (c h2 w2) h w -> b c (h h2) (w w2)', h2=factor, w2=factor)

def squeeze2d_new(input, factor=2):
    return rearrange(input, 'b c (h h2) (w w2) -> b (c h2 w2) h w', h2=factor, w2=factor)
```

