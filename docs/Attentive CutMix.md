---
title: Attentive CutMix
tags: augment
---

# Attentive CutMix
- builds up on CutMix.
- Instead of random pasting, it identifies attentive patches for cutout and pastes them at the same location in the other image.
- avoids the problem of selecting a background region not important for the network and updating the label information
- A separate pre-trained network is employed to extract attentive regions.
- The attention output is mapped back onto the original image

## Backlinks

> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[Attentive CutMix]]

_Backlinks last generated 2022-10-09 12:22:37_
