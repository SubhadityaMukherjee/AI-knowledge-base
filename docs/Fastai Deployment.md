---
title: Fastai Deployment

tags: library 
---

# Fastai Deployment
- [[Gradio]]

## Save

```python
from fastai.vision.widgets import *
```

```python
path = Path()
path.ls(file_exts='.pkl')

learn_inf = load_learner(path/'export.pkl')
learn_inf.predict('images/grizzly.jpg')
learn_inf.dls.vocab
```








## Backlinks

> - [Fastai](fastai.md)
>   - [[Fastai Deployment]]

_Backlinks last generated 2022-07-26 20:33:15_
