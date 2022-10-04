---
tags: temp
title: Cross Validation
date modified: Thursday, August 11th 2022, 12:32:55 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cross Validation

## KFold
- Repeat for m = 1..L
	- Split data into roughly equal sizes. Disjoint subsets
	- Get model with min [[Emperical Risk]]
	- Test it with validation set
	- Avg it for the folds for this value of m
- Find optimal class for that m that had min avg validation risk (aka training error)
- Compute $h_{opt}$ using the original training data

## Leave One Out
- Each D contains a single training example
- For tiny datasets

## Backlinks

> - [Lp [[Regularization]]](Lp Regularization.md)
>   - [[Cross Validation]] required
>    
> - [Tuning Model Flexibility](Tuning Model Flexibility.md)
>   - [[Cross Validation]]
>    
> - [Effects of [[Regularization]]](Effects of Regularization.md)
>   - Current Deep Networks heavily rely on regularizers such as data [[Augmentation]] (DA) or [[Weight Decay]], and employ structural risk minimization, i.e., [[Cross Validation]], to select the optimal [[Regularization|regularization]] hyper-parameters

_Backlinks last generated 2022-10-04 13:01:19_
