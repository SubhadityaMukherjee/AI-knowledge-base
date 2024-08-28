---
toc: true
title: Data Augmentation with Curriculum Learning
categories: ['augment']
date created: Monday, October 10th 2022, 1:58:13 pm
date modified: Monday, October 10th 2022, 2:13:02 pm
---



- @shortenSurveyImageData2019
- [Data Augmentation with Curriculum Learning](Data%20Augmentation%20with%20Curriculum%20Learning.md.md)

## Methods
- [Geometric Transformations](Geometric%20Transformations.md.md)
- [Flipping](Flipping.md.md)
- [Color Space Transform](Color%20Space%20Transform.md)
- [Cropping](Cropping.md.md)
- [Noise Injection](Noise%20Injection.md.md)
- [Color Space Transformations](Color%20Space%20Transformations.md.md)
- [Kernel Filters](Kernel%20Filters.md.md)
- [Feature Space Augmentation](Feature%20Space%20Augmentation.md.md)
- [SMOTE ](SMOTE%20)
- [GAN‐based Data Augmentation](GAN‐based%20Data%20Augmentation.md.md)
- [Meta Learning Data Augmentations](Meta%20Learning%20Data%20Augmentations.md.md)
- [Neural Augmentation](Neural%20Augmentation.md.md)
- [Smart Augmentation](Smart%20Augmentation.md.md)
- [AutoAugment](AutoAugment.md.md)
- [Augmented Random Search](Augmented%20Random%20Search.md.md)
- [Test-time Augmentation](Test-time%20Augmentation.md.md)
- [SamplePairing](SamplePairing.md)
- [Data Augmentation with Curriculum Learning](Data%20Augmentation%20with%20Curriculum%20Learning.md.md)
- [Alleviating Class Imbalance with Data Augmentation](Alleviating%20Class%20Imbalance%20with%20Data%20Augmentation.md.md)

## Discussion
- It is easy to explain the benefit of horizontal [Flipping](Flipping.md.md) or random [cropping](cropping.md.md)
- However, it is not clear why mixing pixels or entire images together such as in PatchShuffle [regularization](regularization.md.md) or SamplePairing is so effective.
- dditionally, it is difficult to interpret the representations learned by neural networks for GAN-based augmentation, variational auto-encoders, and meta-learning.
- An interesting characteristic of these augmentation methods is their ability to be combined together.
- The GAN framework possesses an intrinsic property of recursion which is very interesting
- Samples taken from GANs can be augmented with traditional augmentations such as lighting filters, or even used in neural network augmentation strategies such as [Smart Augmentation](Smart%20Augmentation.md) to create even more samples. These samples can be fed into further GANs and dramatically increase the size of the original dataset.
- An interesting question for practical Data Augmentation is how to determine postaugmented dataset size.
- no consensus about the best strategy for combining data warping and oversampling techniques
- One important consideration is the intrinsic bias in the initial, limited dataset
- There are no existing augmentation techniques that can correct a dataset that has very poor diversity with respect to the testing data



