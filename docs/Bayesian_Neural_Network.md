---
tags: temp
title: Bayesian Neural Network
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Bayesian](Bayesian.md) Neural Network
- [Bayesian_Model_Estimation](Bayesian_Model_Estimation.md)
- Generally we want to learn Joint [Probability](Probability.md) distribution $P(y|x)$ but this does not use the model parameters w
- We need $$P(w|D) = \frac{P(D|w)P(w)}{P(D)}$$
	- D is the labelled dataset
	- Model is now defined by structure and parameters
- The parameters encode information about [Uncertainty](Uncertainty.md)
	- Can be understood using [Bayesian_Predictive_Posterior](Bayesian_Predictive_Posterior.md)
