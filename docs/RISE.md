---
title: RISE

tags: explainability 
date modified: Monday, October 10th 2022, 2:02:08 pm
date created: Thursday, October 6th 2022, 10:51:10 am
---

# RISE
- based on a stochastic approach
- Input images are iteratively altered via random noise, and the final saliency map is composed by accumulating the partial estimations
- However, its application requires much more computational power, as it needs to run hundreds of thousands of prediction cycles
- it seems that RISE is not able to highlight regions of interest of skin lesion images with the same reliability as on pictures of real-world objects
- In the first step, it creates a segmentation mask and applies it to the dermoscopic image. Secondly, it creates a structure segmentation mask to identify the structure of the dermoscopic image. After masking, the original segmented image and some nonvisual metadata are fed into a convolutional neural network for classification

## Backlinks
> - [On the Overlap Between Grad-CAM Saliency Maps and Explainable Visual Features in Skin Cancer Images](On the overlap between Grad-CAM saliency maps and explainable visual features in skin cancer images.md)
>   - [[RISE]]

_Backlinks last generated 2022-10-06 14:20:33_
