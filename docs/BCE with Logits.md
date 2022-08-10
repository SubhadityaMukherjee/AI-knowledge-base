---
title: BCE Logits
tags: loss
date modified: Wednesday, August 10th 2022, 11:41:32 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# BCE Logits
- [Cross Entropy](Cross%20Entropy.md) + logits
$$\left( - \mathrm{sum}\left( y \cdot \mathrm{logsoftmax}\left( ŷ \right) \cdot weight \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

## …

