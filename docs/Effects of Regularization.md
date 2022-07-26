---
title: Effects of Regularization

tags: regularize 
---

# Effects of [[Regularization]]
- [The Effects of Regularization and Data Augmentation are Class Dependent](https://arxiv.org/abs/2204.03632)
- Current Deep Networks heavily rely on regularizers such as data [[Augmentation]] (DA) or [[Weight Decay]], and employ structural risk minimization, i.e., [[Cross Validation]], to select the optimal [[Regularization|regularization]] hyper-parameters
- weight decay increases the average test performances at the cost of significant performance drops on some specific classes
- unfair across classes
- By focusing on maximizing aggregate performance statistics we have produced learning mechanisms that can be potentially harmful, especially in [[Transfer Learning|transfer learning]] tasks
- optimal amount of DA or weight decay found from cross-validation leads to disastrous model performances on some classes
- only by introducing random crop DA during training
- such performance drop also appears when introducing uninformative [[Regularization|regularization]] techniques such as weight decay
- ur search for ever increasing generalization performance – averaged over all classes and samples – has left us with models and regularizers that silently sacrifice performances on some classes.
- varying the amount of [[Regularization|regularization]] employed during pre-training of a specific dataset impacts the per-class performances of that pre-trained model on different downstream tasks e.g. an [[ImageNet]] pre-trained ResNet50 deployed on INaturalist sees its performances fall from 70% to 30% on a particular classwhen introducing random crop DA during the [[ImageNet|Imagenet]] pre-training phase
- designing novel regularizers without class-dependent bias remains an open research question
- Categories largely identifiable by color or texture (for e.g., yellow bird, textured mushroom) are unaffected by aggressive cropping, while categories identifiable by shape (for e.g., corkscrew) see a performance degradation with aggressive cropping that only contains part of the object
- Conversely, color jitter does not affect shape or texture-based categories (for e.g., zebra), but affects color-based categories (for e.g., basket ball)








































































## Backlinks

> - [Regularization](Regularization.md)
>   - [[Effects of Regularization]]

_Backlinks last generated 2022-07-26 20:33:15_
