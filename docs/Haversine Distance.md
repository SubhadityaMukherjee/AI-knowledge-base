---
title: Haversine Distance

tags: distance 
date modified: Thursday, August 11th 2022, 12:32:52 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Haversine Distance
- ![Pasted image 20220624120834](assets/Pasted%20image%2020220624120834.png)
- $$d = 2r\times arcsin(\sqrt{sin^{2}(\frac{\varphi_{2}-\varphi_{1}}{2})+cos(\varphi_{1})cos(\varphi_{2})sin^{2}(\frac{\lambda_{2}-\lambda_{1}}{2}))}$$
- Haversine distance is the distance between two points on a sphere given their longitudes and latitudes
- The main difference is that no straight line is possible since the assumption here is that the two points are on a sphere.
- ssumed the points lie on a sphere
- As you might have expected, Haversine distance is often used in navigation
- calculate the distance between two countries when flying between them
- Note that it is much less suited if the distances by themselves are already not that large. The curvature will not have that large of an impact.

