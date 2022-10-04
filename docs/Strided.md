---
title: Strided
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Strided
- Normally S = 1
- S>1 -> [[Downsampling]]
- Dilated
- Spaces in the filter kernel
- D = 1 : normal [[Conv]] aka D-1 spaces
- Effective Filter size : $$\hat F = F + (F-1)(D-1)$$

