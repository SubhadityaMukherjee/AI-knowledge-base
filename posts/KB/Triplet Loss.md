---
toc: true
title: Triplet Loss
categories: ['loss']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Triplet [Loss](loss.md)
- Given an achor, pull similar closer and push dissimilar away
- Face recog [FaceNet](FaceNet.md)
- Anchor, positive sample are neigbors while neg isnt
- ![im](images/Pasted%20image%2020220310200651.png)
- For each triplet, this condition must hold $$||f(x^a) - f(x^p)||^2 + \alpha \gt f(x^a) - f(x^n)||^2$
- $\alpha$ is a margin b/w positive and neg
- [Loss](loss.md) to minimize $$L(\theta) = \Sigma_i^n||f(x^a) - f(x^p)||^2 + f(x^a) - f(x^n)||^2 + \alpha$
- [Harmonic Triplet Loss](Harmonic%20Triplet%20Loss)



