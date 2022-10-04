---
title: Position Encoding
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:48 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Position Encoding
- Transformers are feed forward. So need a way to inject position into seq
- $$PE(pos, 2i) = sin(\frac{pos}{10000^\frac{2i}{d_{model}}})$$
- $$PE(pos, 2i+1) = cos(\frac{pos}{10000^\frac{2i}{d_{model}}})$$
- Conceptually, adding word order to a sentence
	- Something like ("Hello", 1) , ("from",2) , ("me", 3)

## Backlinks

> - [Basic [[Transformer]]](Basic Transformer.md)
>   - [[Position Encoding]] + [[Token Embedding]]
>    
> - [CvT](CvT.md)
>   - [[Position Encoding]] , a crucial component in existing Vision Transformers, can be safely removed in our model

_Backlinks last generated 2022-10-04 13:01:19_
