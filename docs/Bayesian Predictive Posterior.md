---
tags: temp
title: Bayesian Predictive Posterior
date modified: Thursday, August 11th 2022, 12:32:57 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Bayesian](Bayesian.md) Predictive Posterior
- Follows from [Bayesian Posterior](Bayesian%20Posterior.md)
- Marginalizing over all possible model parameters w
- Computes predictions y with different model parameters w and weights them by the [Probability](Probability.md) of those params given an input x
- [Bayesian](Bayesian.md) Model Averaging
- $$P(y|x) = \int_{w}P(y|w,x)P(w|x)dx$$

