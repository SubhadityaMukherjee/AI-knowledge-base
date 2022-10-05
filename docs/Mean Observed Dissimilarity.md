---
title: Mean Observed Dissimilarity

tags: explainability adversarial 
date modified: Wednesday, October 5th 2022, 3:02:03 pm
date created: Wednesday, October 5th 2022, 3:01:22 pm
---

# Mean Observed Dissimilarity
- is the mean of the NISSIM dissimilarity over the adversarial test set for similar levels of attack.
- So for every adversarial set X ∗, calculate NISSIM value for all samples in that set, and divide by the total number of samples.
- (0,1], such that 0 indicates total similarity while 1 indicates total dissimilarity
- $$MOD_{advset}= \frac{1}{N}\Sigma (NISSIM_{i})$$

## Backlinks

> - [Generalizing Adversarial Explanations with Grad-CAM](Generalizing Adversarial Explanations with Grad-CAM.md)
>   - [[Mean Observed Dissimilarity]]

_Backlinks last generated 2022-10-05 15:25:18_
