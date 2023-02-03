---
title: Random Erasing
tags: augment
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:00:29 pm
---

# Random Erasing
- deletes contiguous rectangular image regions similar to [[cutout]] with minor differences in region selection procedure.
- Opposite to [[cutout]], where deletion is applied on all the images, here it is performed with a probability of either applying it or not
- In every iteration, region size is defined randomly with upper and lower limits on region area and aspect ratio.
- Additional to this, random erasing provides region-aware deletion for object detection and person identification tasks
- Regions inside the object bounding boxes are randomly erased to generate occlusions

## Backlinks

> - [GridMask](GridMask.md)
>   - The algorithm tries to overcome drawbacks of [[Cutout]], [[Random Erasing]], and [[Hide and Seek]] that are prone to deleting important information entirely or leaving it untouched without making it harder for the algorithm to learn.
>    
> - [Comparing Data Augmentation Strategies for Deep Image Classification](Comparing Data Augmentation Strategies for Deep Image Classification.md)
>   - [[Random Erasing]] is useful
>    
> - [SLAK](SLAK.md)
>   - We share the (pre-)training settings of SLaK on ImageNet-1K in this section. We train SLaK for 300 epochs (Section 5.1) and 120 epochs (Section 4) using AdamW (Loshchilov & Hutter, 2019) with a batch size of 4096, and a weight decay of 0.05. The only differnce between models training for 300 epochs and 120 epochs is the training time. The learning rate is 4e-3 with a 20-epoch linear warmup followed by a cosine decaying schedule. For data augmentation, we use the default setting of [[RandAugment]] (Cubuk et al., 2020) in Timm (Wightman, 2019) – "rand-m9-mstd0.5- inc1", Label Smoothing (Szegedy et al., 2016) coefficient of 0.1, Mixup (Zhang et al., 2017) with ↵ = 0.8, [[Cutmix]] (Yun et al., 2019) with ↵ = 1.0, [[Random Erasing]] (Zhong et al., 2020) with p = 0.25, Stochastic Depth with drop rate of 0.1 for SLaK-T, 0.4 for SLaK-S, and 0.5 for SLaK-B, Layer Scale (Touvron et al., 2021c) of initial value of 1e- 6, and EMA with a decay factor of 0.9999. We train SLaK-T with NVIDIA A100 GPUs and the rest of models are trained with NVIDIA V100.

_Backlinks last generated 2023-02-01 13:16:25_
