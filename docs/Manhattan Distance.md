---
title: Manhattan Distance

tags: distance 
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Manhattan Distance
- Taxicab distance or City Block distance, calculates the distance between real-valued vectors
- $$D(x,y) = \Sigma_{i=1}^{k}|x_{i}-y_{i}|$$
- There is no diagonal movement involved in calculating the distance.
- Manhattan distance seems to work okay for high dim data, it is a measure that is somewhat less intuitive than [[Euclidean Distance|euclidean distance]], especially when using in high-dimensional data
- more likely to give a higher distance value than [[Euclidean Distance|euclidean distance]] since it does not the shortest path possible.
- When your dataset has discrete and/or binary attributes, Manhattan seems to work quite well since it takes into account the paths that realistically could be taken within values of those attributes.

## Backlinks

> - [Minkowski Distance](Minkowski Distance.md)
>   - p=1 — [[Manhattan Distance]]
>    
> - [Distance Measures](Distance Measures.md)
>   - [[Manhattan Distance]]

_Backlinks last generated 2022-10-04 13:01:19_
