---
title: Triplet Loss
tags: loss
---

# Triplet Loss
- Given an achor, pull similar closer and push dissimilar away
- Face recog [[FaceNet]]
- Anchor, positive sample are neigbors while neg isnt
- ![[../assets/Pasted image 20220310200651.png]]
- For each triplet, this condition must hold $$||f(x^a) - f(x^p)||^2 + \alpha \gt f(x^a) - f(x^n)||^2$$
- $\alpha$ is a margin b/w positive and neg
- Loss to minimize $$L(\theta) = \Sigma_i^n||f(x^a) - f(x^p)||^2 + f(x^a) - f(x^n)||^2 + \alpha$$
- [[Harmonic Triplet Loss]]






































