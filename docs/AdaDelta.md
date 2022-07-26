---
title: AdaDelta

tags: optimizer gradients 
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

_Backlinks last generated 2022-07-26 20:33:15_
