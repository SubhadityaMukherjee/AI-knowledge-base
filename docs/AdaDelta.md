---
title: AdaDelta

tags: optimizer gradients 
date modified: Thursday, August 11th 2022, 12:32:58 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AdaDelta
- $$RMS[\Delta \theta]_{t}= \sqrt{E[\Delta \theta^{2}]_{t}+ \epsilon}$$
$$\begin{align}\\
& \Delta \theta_{t}= -\frac{RMS[\Delta \theta]_{t-1}}{RMS[g]_{t}}g_{t}\\
& \theta_{t+1}= \theta_{t}+ \Delta \theta_{t}
\end{align}$$

## Backlinks

> - [Gradient Descent #gradients](Gradient Descent gradients.md)
>   - [[AdaDelta]]

_Backlinks last generated 2022-10-04 13:01:19_
