---
title: Color Compositing
tags: visualization
date modified: Thursday, August 11th 2022, 12:32:56 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Color Compositing
- ![[assets/Pasted image 20220418002036.png|im]]
- $$C_{i}= c_{i}+ (1-o_{i})C_{i-1}$$
- where
- $$c_{i}= o_{i}c_{i}'$$
- ![[assets/Pasted image 20220418003237.png|im]]
- First is same as [[Marching Cubes]]
- $$I(p) = \begin{cases*}

f(\sigma)& $\exists t \in [0,T], s(t) = \sigma$ \\

I_{o}&otherwise

\end{cases*}$$

- Higher pixel accurate quality

## Backlinks

> - [Front to Back [[Raycasting]]](Front to Back Raycasting.md)
>   - [[Color Compositing]]
>    
> - [Raycasting](Raycasting.md)
>   - [[Color Compositing]]

_Backlinks last generated 2022-10-04 13:01:19_
