---
title: Color Compositing
tags: visualization
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Color Compositing
- ![im](images/Pasted%20image%2020220418002036.png)
- $$C_{i}= c_{i}+ (1-o_{i})C_{i-1}$$
- where
- $$c_{i}= o_{i}c_{i}'$$
- ![im](images/Pasted%20image%2020220418003237.png)
- First is same as [Marching Cubes](Marching%20Cubes.md)
- $$I(p) = \begin{cases*}

f(\sigma)& $\exists t \in [0,T], s(t) = \sigma$ \\

I_{o}&otherwise

\end{cases*}$$

- Higher pixel accurate quality

