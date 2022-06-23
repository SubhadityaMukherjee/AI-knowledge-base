---
title: Cosine Similarity
tags: loss
---

# Cosine Similarity
- [[Lp Regularization]] l2norm aka p = 2
- Cosine similarity is $$ - \mathrm{sum}\left( \mathrm{l2norm}\left( y \right) \cdot \mathrm{l2norm}\left( ŷ \right) \right)$$
- ![im](assets/Pasted%20Image%2020220506155815.png)
- magnitude of vectors is not taken into account, merely their direction
- In practice, this means that the differences in values are not fully taken into account
- If you take a recommender system, for example, then the cosine similarity does not take into account the difference in rating scale between different users
- high-dimensional data and when the magnitude of the vectors is not of importance


