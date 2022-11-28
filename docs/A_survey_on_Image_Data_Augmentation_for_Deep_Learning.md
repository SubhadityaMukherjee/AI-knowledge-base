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
- [Geometric_Transformations](Geometric_Transformations.md)
- [Flipping](Flipping.md)
- [Color_Space_Transform](Color_Space_Transform.md)
- [Cropping](Cropping.md)
- [Noise_Injection](Noise_Injection.md)
- [Color_Space_Transformations](Color_Space_Transformations.md)
- [Kernel_Filters](Kernel_Filters.md)
- [Feature_Space_Augmentation](Feature_Space_Augmentation.md)
- [SMOTE ](SMOTE%20)
- [GAN‐based_Data_Augmentation](GAN‐based_Data_Augmentation.md)
- [Meta_Learning_Data_Augmentations](Meta_Learning_Data_Augmentations.md)
- [Neural_Augmentation](Neural_Augmentation.md)
- [Smart_Augmentation](Smart_Augmentation.md)
- [AutoAugment](AutoAugment.md)
- [Augmented_Random_Search](Augmented_Random_Search.md)
- [Test-time_Augmentation](Test-time_Augmentation.md)
- [SamplePairing](SamplePairing.md)
- [Data_Augmentation_with_Curriculum_Learning](Data_Augmentation_with_Curriculum_Learning.md)
- [Alleviating_Class_Imbalance_with_Data_Augmentation](Alleviating_Class_Imbalance_with_Data_Augmentation.md)

## Discussion
- It is easy to explain the benefit of horizontal [Flipping](Flipping.md) or random cropping
- However, it is not clear why mixing pixels or entire images together such as in PatchShuffle regularization or SamplePairing is so effective.
- dditionally, it is difficult to interpret the representations learned by neural networks for GAN-based augmentation, variational auto-encoders, and meta-learning.
- An interesting characteristic of these augmentation methods is their ability to be combined together.
- The GAN framework possesses an intrinsic property of recursion which is very interesting
- Samples taken from GANs can be augmented with traditional augmentations such as lighting filters, or even used in neural network augmentation strategies such as Smart Augmentation or Neural Augmentation to create even more samples. These samples can be fed into further GANs and dramatically increase the size of the original dataset.
- An interesting question for practical Data Augmentation is how to determine postaugmented dataset size.
- no consensus about the best strategy for combining data warping and oversampling techniques
- One important consideration is the intrinsic bias in the initial, limited dataset
- There are no existing augmentation techniques that can correct a dataset that has very poor diversity with respect to the testing data
