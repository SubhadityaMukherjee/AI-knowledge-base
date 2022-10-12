---
title: Color Space Transformations
tags: augment
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:12:33 pm
---

# Color Space Transformations
- Image data is encoded into 3 stacked matrices, each of size height×width. These matrices represent pixel values for an individual RGB color value
- Lighting biases are amongst the most frequently occurring challenges to image recognition problems
- A quick fix to overly bright or dark images is to loop through the images and decrease or increase the pixel values by a constant value.
- Another quick color space manipulation is to splice out individual RGB color matrices.
- Another transformation consists of restricting pixel values to a certain min or max value.
- Similar to geometric transformations, a disadvantage of color space transformations is increased memory, transformation costs, and training time.
- Additionally, color transformations may discard important color information and thus are not always a label-preserving transformation.
- For example, when decreasing the pixel values of an image to simulate a darker environment, it may become impossible to see the objects in the image.

