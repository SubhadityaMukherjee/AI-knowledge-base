---
title: Data Augmentation with Curriculum Learning
tags: augment
date created: Monday, October 10th 2022, 1:58:13 pm
date modified: Monday, October 10th 2022, 2:13:02 pm
---

# Data Augmentation with Curriculum Learning
- Connor Shorten and Taghi M. Khoshgoftaar
```toc
```

## Methods
- [[Geometric transformations]]
- [[Flipping]]
- [[Color Space Transform]]
- [[Cropping]]
- [[Noise injection]]
- [[Color space transformations]]
- [[Kernel filters]]
- [[Feature space augmentation]]
- [[SMOTE ]]
- [[GAN‐based Data Augmentation]]
- [[Meta learning Data Augmentations]]
- [[Neural augmentation]]
- [[Smart Augmentation]]
- [[AutoAugment]]
- [[Augmented Random Search]]
- [[Test-time augmentation]]
- [[SamplePairing]]
- [[Data Augmentation with Curriculum Learning]]
- [[Alleviating class imbalance with Data Augmentation]]

## Discussion
- It is easy to explain the benefit of horizontal [[flipping]] or random cropping
- However, it is not clear why mixing pixels or entire images together such as in PatchShuffle regularization or SamplePairing is so effective.
- dditionally, it is difficult to interpret the representations learned by neural networks for GAN-based augmentation, variational auto-encoders, and meta-learning.
- An interesting characteristic of these augmentation methods is their ability to be combined together.
- The GAN framework possesses an intrinsic property of recursion which is very interesting
- Samples taken from GANs can be augmented with traditional augmentations such as lighting filters, or even used in neural network augmentation strategies such as Smart Augmentation or Neural Augmentation to create even more samples. These samples can be fed into further GANs and dramatically increase the size of the original dataset.
- An interesting question for practical Data Augmentation is how to determine postaugmented dataset size.
- no consensus about the best strategy for combining data warping and oversampling techniques
- One important consideration is the intrinsic bias in the initial, limited dataset
- There are no existing augmentation techniques that can correct a dataset that has very poor diversity with respect to the testing data

## Backlinks

> - [](journals/2022-10-10.md)
>   - ## [[A survey on Image Data Augmentation for Deep Learning]]

_Backlinks last generated 2022-10-12 10:22:04_
