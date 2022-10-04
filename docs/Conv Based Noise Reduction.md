---
title: Conv Based Noise Reduction
tags: visualization
date modified: Thursday, August 11th 2022, 12:32:55 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Conv]] Based Noise Reduction
- Noise is high frequency component, suppress via low-pass filters
- Ideal low-pass filter
- multiply with box filter in frequency domain
- convolution with sinc in spatial domain (impractical: infinite extent)
- ![[assets/Pasted image 20220411130419.png|im]]
- ![[assets/Pasted image 20220411130431.png|im]]
- Spatially narrow (wide) filter has wide (narrow) spectrum and low (high) smoothing effect

## Backlinks

> - [Noise Suppression](Noise Suppression.md)
>   - ![[assets/Pasted image 20220418000525.png|im]]- [[Conv Based Noise Reduction]]

_Backlinks last generated 2022-10-04 13:01:19_
