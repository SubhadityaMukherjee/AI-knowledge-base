---
title: Smart Augmentation
tags: augment
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:02:06 pm
---

# Smart Augmentation
- utilizes a similar concept as the [[Neural Augmentation]] technique
- However, the combination of images is derived exclusively from the learned parameters of a prepended CNN, rather than using the Neural Style Transfer algorithm.
- another approach to meta-learning augmentations
- This is done by having two networks, Network-A and Network-B. Network-A is an augmentation network that takes in two or more input images and maps them into a new image or images to train Network-B. The change in the error rate in Network-B is then
- backpropagated to update Network-A.
- Additionally another loss function is incorporated into Network-A to ensure that its outputs are similar to others within the class. Network-A uses a series of convolutional layers to produce the augmented image
- The conceptual framework of Network-A can be expanded to use several Networks trained in parallel. Multiple Network-As could be very useful for learning class-specific augmentations via meta-learning

## Backlinks

> - [AutoAugment](AutoAugment.md)
>   - much different approach to meta-learning than [[Neural Augmentation]] or [[Smart Augmentation]]
>    
> - [[[Data Augmentation with Curriculum Learning]]](A survey on Image Data Augmentation for Deep Learning.md)
>   - Samples taken from GANs can be augmented with traditional augmentations such as lighting filters, or even used in neural network augmentation strategies such as [[Smart Augmentation]] or [[Neural Augmentation]] to create even more samples. These samples can be fed into further GANs and dramatically increase the size of the original dataset.

_Backlinks last generated 2023-01-16 19:40:27_
