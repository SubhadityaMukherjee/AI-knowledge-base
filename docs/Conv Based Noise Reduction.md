---
title: Conv Based Noise Reduction
tags: visualization
date modified: Wednesday, August 10th 2022, 7:05:55 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Conv](Conv.md) Based Noise Reduction
- Noise is high frequency component, suppress via low-pass filters
- Ideal low-pass filter
- multiply with box filter in frequency domain
- convolution with sinc in spatial domain (impractical: infinite extent)
- ![im](assets/Pasted%20image%2020220411130419.png)
- ![im](assets/Pasted%20image%2020220411130431.png)
- Spatially narrow (wide) filter has wide (narrow) spectrum and low (high) smoothing effect

