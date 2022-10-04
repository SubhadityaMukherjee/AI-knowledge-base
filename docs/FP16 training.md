---
tags: temp
title: FP16 training
date modified: Thursday, August 11th 2022, 12:32:54 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FP16 Training
- Reduced precision has a narrower range that might make the results more out of range and worsen the training progress
- Can store all parameters and activations in FP16 and then use that for gradients.
- Also copy to FP32 for parameter updates
- Multiply scalar to loss to align range of FP16

## Backlinks

> - [Google NMT](Google NMT.md)
>   - low-precision arithmetic during inference computations ([[FP16 training]] ???)

_Backlinks last generated 2022-10-04 13:01:19_
