---
title: Strided
tags: architecture 
date modified: Wednesday, August 10th 2022, 7:05:46 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Strided
- Normally S = 1
- S>1 -> Downsampling
- Dilated
- Spaces in the filter kernel
- D = 1 : normal [Conv](Conv.md) aka D-1 spaces
- Effective Filter size : $$\hat F = F + (F-1)(D-1)$$

