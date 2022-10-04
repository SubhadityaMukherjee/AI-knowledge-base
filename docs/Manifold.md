---
tags: temp
title: Manifold
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Manifold
- Data manifolds are an abstraction
- Only geometric insights are important
- Locally around some point c where the [[PDF]] is large -> It will stay large only for a small fraction of directions
	- Those directions span a low dimensional hyperplane around c
	- "low dimensional sheets"
	- curved path
- In an n dimensional real vector space $\mathbb{R}^{n}$ . [[Embedding]] space
	- $m \leq n$ is a positive integer
	- An m dim manifold $\mathcal{M}$ is a subset of the vector space where one can smoothly map a neighborhood of that point to a neighborhood of the origin in m dim Euclidean space
		- Locally represents Euclidean space
- Only surface and not interior
- No sharp edges or spikes
- Can be exploited by [[Adversarial Learning]]
- Examples
	- 1 dim -> Lines in some high dim figure : B
	- 2 dim -> Surfaces : A
	- ![[assets/Pasted image 20220316181643.png|im]]
	- ![[assets/Pasted image 20220316181947.png|im]]
	- ![[assets/Pasted image 20220316182354.png|im]]
	- ![[assets/Pasted image 20220316182449.png|im]]

## Refs
- [tds](https://towardsdatascience.com/manifolds-in-data-science-a-brief-overview-2e9dde9437e5)
- [way more stuff : bjlkeng](https://bjlkeng.github.io/posts/manifolds/) #todo

## Backlinks

> - [Adversarial Learning](Adversarial Learning.md)
>   - Consider data in a [[Manifold]]. The [[PDF]] is concentrated along a low dim [[Manifold]] $\mathcal{M}$
>   - Consider data in a [[Manifold]]. The [[PDF]] is concentrated along a low dim [[Manifold]] $\mathcal{M}$
>   - Now the original picture is a point on the [[Manifold]] (dim = output layer size)
>    
> - [Challenge of Complex Geometry](Complex Geometry.md)
>   - [[Manifold]]

_Backlinks last generated 2022-10-04 13:01:19_
