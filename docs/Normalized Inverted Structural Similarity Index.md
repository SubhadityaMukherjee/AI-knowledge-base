---
title: Normalized Inverted Structural Similarity Index

tags: explainability adversarial 
date modified: Monday, October 10th 2022, 2:02:08 pm
date created: Wednesday, October 5th 2022, 2:55:16 pm
---

# Normalized Inverted [[Structural Similarity Index]]
- metric is calculated from [[Structural Similarity Index]] by inverting the range and then normalizing it.
- NISSIM bounds to (0, 1] where 0 means similar and 1 means dissimilar. Ideally we want this value as close to 0 as possible
- $$NISSIM_{i}= \frac{1-SSIM_{i}}{2}$$

## Backlinks
> - [Generalizing Adversarial Explanations with Grad-CAM](Generalizing Adversarial Explanations with Grad-CAM.md)
>   - These metrics are computed by comparing a [[Normalized Inverted Structural Similarity Index]] (NISSIM) metric of the Grad-CAM generated heatmap for samples from the original test set and samples from the adversarial test set.
>   - [[Normalized Inverted Structural Similarity Index]]

_Backlinks last generated 2022-10-05 15:25:18_
