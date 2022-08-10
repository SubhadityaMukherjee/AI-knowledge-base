---
title: Opacity Correction
tags: visualization
date modified: Wednesday, August 10th 2022, 11:41:25 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Opacity Correction
- Opacity component $o$ in transfer function stored with respect to a standard step size $\Delta t$
- Different step sizes $\Delta t^{\ast}$
- Dynamic step sizes
- generate pre-integrated function
- $$o^{\ast} = 1- (1-o)^{\frac{\Delta t^{\ast}}{\Delta t}}$$
- evaluate after obtaining $o$ from transfer function
- apply before compositing`

