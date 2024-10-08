---
tags: ['temp']
toc: true
title: Bayesian Predictive Posterior
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Bayesian]] Predictive Posterior
- Follows from [[Bayesian Posterior]]
- Marginalizing over all possible model parameters w
- Computes predictions y with different model parameters w and weights them by the [[Probability]] of those params given an input x
- [[Bayesian]] Model Averaging
- $$P(y|x) = \int_{w}P(y|w,x)P(w|x)dx$$



