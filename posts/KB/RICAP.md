---
toc: true
title: RICAP
categories: ['augment']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# RICAP
- @takahashiDataAugmentationUsing2020
- Random image [cropping](cropping.md) and patching
- [cropping](cropping.md) four regions from randomly sampled images and augmenting them to create a new image.
- The generated image has mixed labels proportional to the pasted area
- The area of cropped regions in the output image is determined by sampling through uniform distribution
- anywhere-RICAP (origin can be anywhere), center-RICAP (origin can only be in the middle of the image), and corner-RICAP (origin can only be in corners
- Corner-RICAP has shown the best performance because a larger region of one image is visible to the network to learn



