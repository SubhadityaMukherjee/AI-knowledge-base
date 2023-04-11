---
title: Attentive CutMix
tags: augment
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Attentive [[CutMix]]
- @walawalkarAttentiveCutMixEnhanced2020
- builds up on [[CutMix]] .
- Instead of random pasting, it identifies attentive patches for [[cutout]] and pastes them at the same location in the other image.
- avoids the problem of selecting a background region not important for the network and updating the label information
- A separate pre-trained network is employed to extract attentive regions.
- The attention output is mapped back onto the original image

