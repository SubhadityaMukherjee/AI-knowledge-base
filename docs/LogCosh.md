---
title: Log Cosh
tags: loss
---

# Log Cosh
- works like the [[MSE]], but is smoothed towards large errors (presumably caused by outliers) so that the final error score isn’t impacted thoroughly.

We first define the [[softplus]] function $$\log\left( e^{x} + 1 \right)$$

Then , $$x = ŷ - y$$

logcosh = $$\mathrm{mean}\left( x + \mathrm{softplus}\left( -2 \cdot x \right) - \log\left( 2.0 \right) \right)$$

## …


























































































