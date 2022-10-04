---
title: Uniform Sampling
tags: distribution 
date modified: Thursday, August 11th 2022, 12:32:44 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Uniform [[Sampling]]
- Random [[Sampler]]
- [[Uniform Distribution]]
- If need to sample from another distribution with a [[PDF]] f(x). Can use a uniform [[Sampler]] on the distribution [0,1] to indirectly sample from it
	- Coordinate transform
	- [[CDF]]
	- Get a [[Sampler]] for by $$X_{i} = \varphi^{-1}\circ U_{i}$$
	- ![[assets/Pasted image 20220324113838.png|im]]

