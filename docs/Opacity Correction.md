---
title: Opacity Correction
tags: visualization
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Opacity Correction
- Opacity component $o$ in [[Transfer Function|transfer function]] stored with respect to a standard step size $\Delta t$
- Different step sizes $\Delta t^{\ast}$
- Dynamic step sizes
- generate pre-integrated function
- $$o^{\ast} = 1- (1-o)^{\frac{\Delta t^{\ast}}{\Delta t}}$$
- evaluate after obtaining $o$ from [[Transfer Function|transfer function]]
- apply before compositing`

## Backlinks
> - [Transfer Function](Transfer Function.md)
>   - [[Opacity Correction]]

_Backlinks last generated 2022-10-04 13:01:19_
