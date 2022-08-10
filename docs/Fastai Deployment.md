---
title: Fastai Deployment

tags: library 
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Fastai Deployment
- [Gradio](Gradio.md)

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

