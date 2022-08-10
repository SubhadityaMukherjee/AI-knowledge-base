---
tags: temp
title: FP16 training
date modified: Wednesday, August 10th 2022, 11:41:29 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FP16 Training
- Reduced precision has a narrower range that might make the results more out of range and worsen the training progress
- Can store all parameters and activations in FP16 and then use that for gradients.
- Also copy to FP32 for parameter updates
- Multiply scalar to loss to align range of FP16

