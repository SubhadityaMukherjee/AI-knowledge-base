---
title: Color Compositing
---

# Color Compositing
- ![[Pasted image 20220418002036.png]]
- $$C_{i}= c_{i}+ (1-o_{i})C_{i-1}$$
- where 
- $$c_{i}= o_{i}c_{i}'$$
- ![[Pasted image 20220418003237.png]]
- First is same as [[Marching Cubes]]
	- $$I(p) = \begin{cases*}

f(\sigma)&  $\exists t \in [0,T], s(t) = \sigma$ \\

I_{o}&otherwise

\end{cases*}$$
	- Higher pixel accurate quality


## Backlinks
* [[Raycasting]]
	* [[Color Compositing]]
* [[Front to Back Raycasting]]
	* [[Color Compositing]]
