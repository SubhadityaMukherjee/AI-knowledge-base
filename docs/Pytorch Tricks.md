---
title: Pytorch Tricks

tags: library 
---

# Pytorch Tricks

## Get Params of a Layer
```python
m = learn.model
l = m.get_submodule('0.model.stem.1')
list(l.parameters())
```

## Interact
```python
from ipywidgets import interact
@interact(m=1.5, b=1.5)
def plot_relu(m,b):
	plot_function(partial(relu, m, b), ylim = (-1, 4))
```


## Backlinks

> - [](journals/2022-07-25.md)
>   - [[Pytorch Tricks]]

_Backlinks last generated 2022-07-25 17:11:34_
