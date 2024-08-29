---
title: Chapter 5 - Loss functions
toc: true
tags:
  - deeplearning
  - loss
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Chapter 5 - Loss Functions
```toc
```
- A large list of useful loss functions can be found [[loss]]
- A large list of useful distributions can be found here [[distributions]]
- A loss function or cost function L[φ] returns a single number that describes the mismatch between the model predictions f[xi, φ] and their corresponding ground-truth outputs $y_i$

## Distributions
- ![[Pasted image 20240828112456.png]]

## Maximum Likelihood
### [[Log Likelihood Loss.md]]
### [[Maximum Likelihood.md]]

## Constructing New Loss Functions
### [[Recipe for constructing loss functions.md]]

### [[Loss for univariate regression.md]]

### [[Loss for binary classification.md]]

### [[Loss for multiclass classification.md]]

- Difference between the distributions : [[../../KB/KL Divergence|KL Divergence]] or [[../../KB/Cross Entropy|Cross Entropy]]

### For Multimodal
- Fusion loss
- Multiple attention heads : backprop from heads
## Other Notes
- [[heteroscedastic nonlinear regression.md]]
- [[Robust regression.md]]
- [[Quantile Regression.md]]
- [[Focal Loss.md]]
- [[Van Mises distribution.md]]
- Non probabilistic approaches - [[Hinge Loss.md]], [[AdaBoost]]