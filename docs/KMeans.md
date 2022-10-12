---
tags: temp
title: K Means
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# K Means
- Codebook vectors. No manifolds.
- Given: $$(x_i)_{i= 1,..,N} \in \mathbb{R}^n$$
- Need : K clusters $$C_1 , … , C_K$$
- Randomly assign training points to K sets : $$S_j (j = 1, …, K)$$
- Repeat:
	- For each set $$S_j$$
		- Mean $$\mu_j = |S_j|^{-1} \Sigma_{x \in S_j} x$$
		- Create new sets by putting points into set where $||x_i-\mu_j||$ is minimal
		- If empty, dismiss and reduce K to K'
- Error quantity does not increase
	- [[Intra cluster variance]]
	- Clusters are bounded by line [[Decision Boundaries]] and forms a [[Voronoi Cell]]
- Does not work for curved boundaries

## Codebook Vector
- Each cluster represented by it
- Vector pointing to the mean of all vectors in the cluster
- Center of [[gravity]]

## Backlinks
> - [Dimensionality Reduction](Dimensionality Reduction.md)
>   - [[KMeans]]
>
> - [Clustering](Clustering.md)
>   - [[KMeans]]

_Backlinks last generated 2022-10-04 13:01:19_
