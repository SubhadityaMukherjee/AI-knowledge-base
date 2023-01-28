---
title: Proxy Attention

tags: mastersthesis explainability 
date modified: Friday 27th January 2023, Fri
date created: Friday 27th January 2023, Fri
---

# Proxy Attention
```toc
```

## Comparisons
- [[M2Det]] 
	- The Multi-level Feature Pyramid Network has similar ideas but does not use the outputs of XAI algorithms. 
	- This uses channel wise attention : ours is independant of that
	- This takes images and passes them through multiple networks and then aggregates the features obtained from each of those networks. : ours uses a trained network and is independent of all that. Unlike the former, ours does not use a compressed feature map but uses a trained network to predict an explainability map instead.

## Backlinks

> - [Vision Explainibility](Vision Explainibility.md)
>   - [[Proxy Attention]]

_Backlinks last generated 2023-01-28 14:37:47_
