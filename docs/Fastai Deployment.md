---
title: Fastai Deployment

tags: library 
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[fastai|Fastai]] Deployment
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

_Backlinks last generated 2022-10-04 13:01:19_
