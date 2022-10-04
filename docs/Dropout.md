---
title: Dropout
tags: regularize
date modified: Thursday, August 11th 2022, 12:32:54 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Dropout
- Applied to [[Dense]] [[Layers]]
- Training : Randomly (Bernoulli, p = 0.5 say) set #activations to 0
- Generally p = 0.1, 0.5
- Testing: Reweight by p
	- Because after training values will increase by $$1/(1-p)$$
- Reduces co dependence between neurons
- Decreases overfitting
- Start with small rate : 20 %
- Helps with small datasets
- Reducing [[Co adaptation]] by making the presence of other hidden [neurons] unreliable
- The authors found that there is a trade-off between when Dropout is necessary, and when it's no longer useful. First, to cover the case where the dataset is extremely small: even Dropout does not improve performance in that case, simply because the dataset size is too small. The same is true for datasets that are large enough: Dropout then does no longer improve the model, but rather, model performance gets worse.

