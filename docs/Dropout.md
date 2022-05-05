---
title: Dropout
tags: regularize
---

# Dropout
- Applied to [[Dense]] [[layers]]
- Training : Randomly (Bernoulli, p = 0.5 say) set #activations to 0
- Generally p = 0.1, 0.5
- Testing: Reweight by p
	- Because after training values will increase by $$1/(1-p)$$
- Reduces co dependence between neurons
- Decreases overfitting
- Start with small rate : 20 %








