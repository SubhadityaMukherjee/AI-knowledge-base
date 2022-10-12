---
title: Co adaptation

tags: optimizer gradients 
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Co Adaptation
- Computing the gradient is done with respect to the error, but also with respect to what all other units are doing (Srivastava et al., 2014). This means that certain neurons, through changes in their weights, may fix the mistakes of other neurons. These, Srivastava et al. (2014) argue, lead to complex co-adaptations that may not generalize to unseen data, resulting in overfitting.

## Backlinks
> - [Dropout](Dropout.md)
>   - Reducing [[Co adaptation]] by making the presence of other hidden [neurons] unreliable

_Backlinks last generated 2022-10-04 13:01:19_
