---
title: Chapter 5 - Loss functions
toc: true
tags:
  - deeplearning
  - loss
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Chapter 5 - Loss functions
```toc
```
- A large list of useful loss functions can be found [[Tag Pages/loss|loss]]
- A large list of useful distributions can be found here [[distribution]]
- A loss function or cost function L[φ] returns a single number that describes the mismatch between the model predictions f[xi, φ] and their corresponding ground-truth outputs $y_i$

## Distributions
- ![[../../images/Pasted image 20240828112456.png]]

## Maximum likelihood
### [[Log Likelihood Loss.md]]
### [[Maximum Likelihood.md]]

## Constructing new loss functions
### [[Recipe for constructing loss functions.md]]

### [[Loss for univariate regression.md]]

### [[Loss for binary classification.md]]

### [[Loss for multiclass classification.md]]

- Difference between the distributions : [[../../KB/KL Divergence|KL Divergence]] or [[../../KB/Cross Entropy|Cross Entropy]]

### For multimodal
- Fusion loss
- Multiple attention heads : backprop from heads
## Other notes
- [[heteroscedastic nonlinear regression.md]]
- [[Robust regression.md]]
- [[Quantile Regression.md]]
- [[Focal Loss.md]]
- [[Van Mises distribution.md]]
- Non probabilistic approaches - [[Hinge Loss.md]], [[AdaBoost]]