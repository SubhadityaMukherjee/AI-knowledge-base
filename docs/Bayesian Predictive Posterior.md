---
tags: temp
title: Bayesian Predictive Posterior
date modified: Thursday, August 11th 2022, 12:32:57 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Bayesian]] Predictive Posterior
- Follows from [[Bayesian Posterior]]
- Marginalizing over all possible model parameters w
- Computes predictions y with different model parameters w and weights them by the [[Probability]] of those params given an input x
- [[Bayesian]] Model Averaging
- $$P(y|x) = \int_{w}P(y|w,x)P(w|x)dx$$

## Backlinks

> - [[[Bayesian]] Neural Network](Bayesian Neural Network.md)
>   - Can be understood using [[Bayesian Predictive Posterior]]

_Backlinks last generated 2022-10-04 13:01:19_
