---
title: Fastai Deployment

tags: library 
date modified: Wednesday, August 10th 2022, 11:41:29 am
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

