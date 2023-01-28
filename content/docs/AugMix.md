---
title: AugMix
tags: augment
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# AugMix
- using the input image itself
- t transforms (translate, shear, rotate and etc) the input image and mixes it with the original image
- Image transformation involves series of randomly selected augmentation operations applied with three parallel augmentation chains.
- Each chain has a composition of operations that could involve applying, for example, translation on input image followed by shear and so on
- The output of these three chains is three images mixed to form a new image.
- This new image is later mixed with the original image to generate the final augmented output image,

