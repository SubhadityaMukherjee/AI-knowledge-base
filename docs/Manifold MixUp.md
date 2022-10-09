---
title: Manifold MixUp
tags: augment
---

# Manifold MixUp
- mixes feature values generated from intermediate neural network layers.
- feedforward up to k layer of the network where the output feature maps are mixed
- The mixed feature maps are given input to the next layer and forward propagated up to the last layer.
- After the forward propagation, backward propagation is performed in the standard way with updated labels

## Backlinks

> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[Manifold MixUp]]

_Backlinks last generated 2022-10-09 12:22:37_
