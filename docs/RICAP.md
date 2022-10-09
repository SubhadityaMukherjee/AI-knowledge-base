---
title: RICAP
tags: augment
---

# RICAP
- Random image cropping and patching
- cropping four regions from randomly sampled images and augmenting them to create a new image.
- The generated image has mixed labels proportional to the pasted area
- The area of cropped regions in the output image is determined by sampling through uniform distribution
- anywhere-RICAP (origin can be anywhere), center-RICAP (origin can only be in the middle of the image), and corner-RICAP (origin can only be in corners
- Corner-RICAP has shown the best performance because a larger region of one image is visible to the network to learn

## Backlinks

> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[RICAP]]

_Backlinks last generated 2022-10-09 12:22:37_
