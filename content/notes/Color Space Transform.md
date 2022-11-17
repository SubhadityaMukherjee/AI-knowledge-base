---
title: Color Space Transform
tags: augment
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:00:40 pm
---

# Color Space Transform
- Digital image data is usually encoded as a tensor of the dimension (height × width × color channels)
- Performing augmentations in the color channels space is another strategy that is very practical to implement.
- Very simple color augmentations include isolating a single color channel such as R, G, or B.
- An image can be quickly converted into its representation in one color channel by isolating that matrix and adding 2 zero matrices from the other color channels. Additionally, the RGB values can be easily manipulated with simple matrix operations to increase or decrease the brightness of the image.
- More advanced color augmentations come from deriving a color histogram describing the image

