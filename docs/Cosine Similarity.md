---
title: Cosine Similarity
tags: distance loss
date modified: Thursday, August 11th 2022, 12:32:55 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cosine Similarity
- [[Lp Regularization]] l2norm aka p = 2
- Cosine similarity is $$ - \mathrm{sum}\left( \mathrm{l2norm}\left( y \right) \cdot \mathrm{l2norm}\left( ŷ \right) \right)$$
- ![[assets/Pasted image 20220506155815.png|im]]
- magnitude of vectors is not taken into account, merely their direction
- In practice, this means that the differences in values are not fully taken into account
- If you take a [[Recommender System|recommender system]], for example, then the cosine similarity does not take into account the difference in rating scale between different users
- high-dimensional data and when the magnitude of the vectors is not of importance

## Backlinks

> - [Distance Measures](Distance Measures.md)
>   - [[Cosine Similarity]]

_Backlinks last generated 2022-10-04 13:01:19_
