---
title: Uniform Sampling
tags: distribution 
date modified: Thursday, August 11th 2022, 12:32:44 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Uniform [Sampling](Sampling)
- Random [Sampler](Sampler.md)
- [Uniform Distribution](Uniform%20Distribution.md)
- If need to sample from another distribution with a [PDF](PDF.md) f(x). Can use a uniform [Sampler](Sampler.md) on the distribution [0,1] to indirectly sample from it
	- Coordinate transform
	- [CDF](CDF.md)
	- Get a [Sampler](Sampler.md) for by $$X_{i} = \varphi^{-1}\circ U_{i}$$
	- ![im](assets/Pasted%20image%2020220324113838.png)

