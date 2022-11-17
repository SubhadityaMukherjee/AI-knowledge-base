---
title: Cosine Similarity
tags: distance loss
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cosine Similarity
- [Lp Regularization](Lp%20Regularization.md) l2norm aka p = 2
- Cosine similarity is $$ - \mathrm{sum}\left( \mathrm{l2norm}\left( y \right) \cdot \mathrm{l2norm}\left( ŷ \right) \right)$$
- ![im](images/Pasted%20image%2020220506155815.png)
- magnitude of vectors is not taken into account, merely their direction
- In practice, this means that the differences in values are not fully taken into account
- If you take a [recommender system](Recommender%20System.md), for example, then the cosine similarity does not take into account the difference in rating scale between different users
- high-dimensional data and when the magnitude of the vectors is not of importance

