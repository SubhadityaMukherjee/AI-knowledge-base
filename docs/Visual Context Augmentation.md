---
title: Visual Context Augmentation
tags: augment
---

# Visual Context Augmentation
- learns to place object instances at an image location depending on the surrounding context.
- A neural network is trained for this purpose.
- The training data is pre- pared to generate a context image with the masked- out object inside it.
- From an image, 200 context sub-images are generated surrounding the blacked- out bounding box. The neural network learns to predict the category (object or background) in masked pixels.
- The object instances are placed inside the selected boxes to generate a new train- ing image

## Backlinks

> - [RandAugment](RandAugment.md)
>   - [[Augmentation]]
>    
> - [BYOL](BYOL.md)
>   - dependent on existing sets of [[Augmentation]] that are specific to vision applications
>    
> - [](DeepLearning.md)
>   - [[Augmentation]]
>    
> - [Non [[Relational Inductive Bias]]](Non Relational Inductive Bias.md)
>   - [[Augmentation]]
>    
> - [Regularization](Regularization.md)
>   - [[Augmentation]]
>    
> - [Effects of [[Regularization]]](Effects of Regularization.md)
>   - Current Deep Networks heavily rely on regularizers such as data [[Augmentation]] (DA) or [[Weight Decay]], and employ structural risk minimization, i.e., [[Cross Validation]], to select the optimal [[Regularization|regularization]] hyper-parameters
>    
> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[Visual Context Augmentation]]
>    
> - [Noise](Adding noise.md)
>   - [[Augmentation]]

_Backlinks last generated 2022-10-09 12:22:37_
