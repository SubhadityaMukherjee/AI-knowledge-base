---
title: Triplet Loss
tags: loss
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Triplet [[loss|Loss]]
- Given an achor, pull similar closer and push dissimilar away
- Face recog [[FaceNet]]
- Anchor, positive sample are neigbors while neg isnt
- ![[assets/Pasted image 20220310200651.png|im]]
- For each triplet, this condition must hold $$||f(x^a) - f(x^p)||^2 + \alpha \gt f(x^a) - f(x^n)||^2$
- $\alpha$ is a margin b/w positive and neg
- [[loss|Loss]] to minimize $$L(\theta) = \Sigma_i^n||f(x^a) - f(x^p)||^2 + f(x^a) - f(x^n)||^2 + \alpha$
- [[Harmonic Triplet Loss]]

## Backlinks

> - [Semi Supervised](Semi Supervised.md)
>   - [[Triplet Loss]]
>    
> - [FaceNet](FaceNet.md)
>   - FaceNet directly trains its output to be a compact 128-D [[Embedding|embedding]] using a [[Triplet Loss]] function
>    
> - [Feature Learning](Feature Learning.md)
>   - [[Triplet Loss]]

_Backlinks last generated 2022-10-04 13:01:19_
