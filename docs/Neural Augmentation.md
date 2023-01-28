---
title: Neural Augmentation
tags: augment
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:02:06 pm
---

# Neural Augmentation
- The Neural Style Transfer algorithm requires two parameters for the weights of the style and content loss. Perez and Wang presented an algorithm to meta-learn a Neural Style Transfer strategy called Neural Augmentation.
- e Neural Augmentation approach takes in two random images from the same class. The prepended augmentation net maps them into a new image through a CNN with 5 layers, each with 16 channels, 3×3 filters, and ReLU activation functions. The image outputted from the augmentation is then transformed with another random image via Neural Style Transfer.
- This style transfer is carried out via the CycleGAN extension of the GAN framework
- These images are then fed into a classification model and the error from the classification model is backpropagated to update the Neural Augmentation net.
- The Neural Augmentation network uses this error to learn the optimal weighting for content and style images between different images as well as the mapping between images in the CNN
- The Neural Augmentation techniques tested consist of three levels based on the design of the loss function for the augmentation net (Content loss, Style loss via gram matrix, and no loss computer at this layer)

## Backlinks

> - [AutoAugment](AutoAugment.md)
>   - much different approach to meta-learning than [[Neural Augmentation]] or [[Smart Augmentation]]
>    
> - [[[Data Augmentation with Curriculum Learning]]](A survey on Image Data Augmentation for Deep Learning.md)
>   - Samples taken from GANs can be augmented with traditional augmentations such as lighting filters, or even used in neural network augmentation strategies such as [[Smart Augmentation]] or [[Neural Augmentation]] to create even more samples. These samples can be fed into further GANs and dramatically increase the size of the original dataset.
>    
> - [Smart Augmentation](Smart Augmentation.md)
>   - utilizes a similar concept as the [[Neural Augmentation]] technique

_Backlinks last generated 2023-01-28 14:37:47_
