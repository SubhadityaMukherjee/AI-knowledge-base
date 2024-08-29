---
toc: true
title: Data Augmentation with Curriculum Learning
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:13 pm
date modified: Monday, October 10th 2022, 2:13:02 pm
---



- @shortenSurveyImageData2019
- [[Data Augmentation with Curriculum Learning.md|Data Augmentation with Curriculum Learning]]

## Methods
- [[Geometric Transformations.md|Geometric Transformations]]
- [[Flipping.md|Flipping]]
- [[Color Space Transform.md|Color Space Transform]]
- [[Cropping.md|Cropping]]
- [[Noise Injection.md|Noise Injection]]
- [[Color Space Transformations.md|Color Space Transformations]]
- [[Kernel Filters.md|Kernel Filters]]
- [[Feature Space Augmentation.md|Feature Space Augmentation]]
- [[SMOTE ]]
- [[GAN‐based Data Augmentation.md|GAN‐based Data Augmentation]]
- [[Meta Learning Data Augmentations.md|Meta Learning Data Augmentations]]
- [[Neural Augmentation.md|Neural Augmentation]]
- [[Smart Augmentation.md|Smart Augmentation]]
- [[AutoAugment.md|AutoAugment]]
- [[Augmented Random Search.md|Augmented Random Search]]
- [[Test-time Augmentation.md|Test-time Augmentation]]
- [[SamplePairing.md|SamplePairing]]
- [[Data Augmentation with Curriculum Learning.md|Data Augmentation with Curriculum Learning]]
- [[Alleviating Class Imbalance with Data Augmentation.md|Alleviating Class Imbalance with Data Augmentation]]

## Discussion
- It is easy to explain the benefit of horizontal [[Flipping.md|Flipping]] or random [[cropping.md|cropping]]
- However, it is not clear why mixing pixels or entire images together such as in PatchShuffle [[regularization.md|regularization]] or SamplePairing is so effective.
- dditionally, it is difficult to interpret the representations learned by neural networks for GAN-based augmentation, variational auto-encoders, and meta-learning.
- An interesting characteristic of these augmentation methods is their ability to be combined together.
- The GAN framework possesses an intrinsic property of recursion which is very interesting
- Samples taken from GANs can be augmented with traditional augmentations such as lighting filters, or even used in neural network augmentation strategies such as [[Smart Augmentation.md]] to create even more samples. These samples can be fed into further GANs and dramatically increase the size of the original dataset.
- An interesting question for practical Data Augmentation is how to determine postaugmented dataset size.
- no consensus about the best strategy for combining data warping and oversampling techniques
- One important consideration is the intrinsic bias in the initial, limited dataset
- There are no existing augmentation techniques that can correct a dataset that has very poor diversity with respect to the testing data



