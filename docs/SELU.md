---
title: SELU

tags: activations 
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# SELU
- $$selu(x) = \lambda x , \text{if } x >0 , \text{else }, \alpha(e^{x}-1)$$

## Information
- Paper: [https://arxiv.org/pdf/1706.02515.pdf](https://arxiv.org/pdf/1706.02515.pdf)
- scaled variant of the [[Elu]] function
- does internal normalization ("self-normalizing")
    - each layer preserves the mean and the variance from the previous one
    - normalization happens within the activation function
    - to work:
        - input features must be standardized
        - architecture must be sequential
            - self-normalizing not guaranteed otherwise
        - SELU as activation 
        - custom [[Initialization]]
            - zero mean
            - [[Standard Deviation|standard deviation]]: $\sqrt{\frac{1}{ \#inputs}}$
        - if all [[Layers|layers]] are dense (in paper), but other research showed that it also works for CNNs
- has two fixed parameters α and λ
    - not hyperparameters nor learnt parameters
    - derived from the inputs (μ=0, std=1)
    - α≈1.6732, λ≈1.0507
- Pros:
    - no [[Vanishingexploding gradients]]
    - cannot die as [[Relu]]
    - converges faster and to a better result than other activation functions
    - significantly outperformed other activation functions for deep networks
- Cons:
	- Computational heavier

## Backlinks
> - [](ActivationFunctions.md)
>   - [[SELU]] > [[Elu]] > [[Leaky Relu]] > [[Relu]] > [[Tanh]] > [[Sigmoid]]

_Backlinks last generated 2022-10-04 13:01:19_
