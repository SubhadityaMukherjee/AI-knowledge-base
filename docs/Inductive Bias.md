---
title: Inductive Bias
tags: temp
date modified: Thursday, August 11th 2022, 12:32:52 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Inductive Bias
- Set of assumptions that the learner uses to predict outputs of given inputs that it has not yet encountered
- In [[Bayesian]]
	- [[Bayesian Prior]] can shape the [[Bayesian Posterior]] in the way that it can be a similar distribution to the former
- In [[KNN]]
	- we assume that similar data points are clustered near each other away from the dissimilar ones
- in [[LinearRegression]]
	- we assume that the variable Y is linearly dependent on the explanatory variables X.
	- Therefore, the resulting model linearly fits the training data. However, this assumption can limit the model’s capacity to learn non-linear functions.
- in [[Logistic Regression]]
	- assume that there’s a hyperplane that separates the two classes from each other. This simplifies the problem, but one can imagine that if the assumption is not valid, we won’t have a good model.
- [[Non Relational Inductive Bias]]
- [[Relational Inductive Bias]]

