---
title: Focal Loss
tags: loss
---

# Focal Loss
- two-stage approach popularized by R-CNN, where a classifier is applied to a sparse set of candidate object locations.
- In contrast, one-stage detectors that are applied over a regular, [dense](Dense.md) sampling of possible object locations have the potential to be faster and simpler, but have trailed the accuracy of two-stage detectors thus far.
- Extreme foreground-background class imbalance encountered during training of [dense](Dense.md) detectors is the central cause
- modulating term to [[Cross Entropy]] in order to focus learning on hard misclassified examples
- scaling factor decays to zero as confidence in the correct class increases
- training on a sparse set of hard examples and prevents the vast number of easy negatives from overwhelming the detector during training
- [[RetinaNet]]








































