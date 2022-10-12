---
title: Xavier Initialization
tags: regularize 
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Xavier [[Initialization]]
- $$\mathrm{a=\sqrt{\frac{6}{\left(\mathrm{d}\mathrm{_{\mathrm{in}}^{\mathrm{ }}}+\mathrm{d}_{\mathrm{out}} \right)}}}$$
- Random values drawn uniformly from $[-a,a]$
- For [[Batch Normalization]] [[Layers]], $\gamma =1$ and $\beta=0$
- For [[Tanh]] based activating neural nets

## Backlinks
> - [Initialization](Initialization.md)
>   - [[Xavier Initialization]] , [[He Initialization]] , [[LeCun Init]]

_Backlinks last generated 2022-10-04 13:01:19_
