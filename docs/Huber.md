---
title: Huber/Smooth L1/Smooth MAE
tags: loss
---

# Huber/Smooth L1/Smooth MAE
- It is less sensitive to outliers than the [[MSE]] and in some cases prevents exploding #gradients
- [[Fast-RCNN]]

if $$\left( \left\|y - ŷ\right\| \lt 1.0 \right) >1 $$

$$\frac{1}{\mathrm{length}\left( y \right)} \cdot \mathrm{sum}\left( 0.5 \cdot \left( y - ŷ \right)^{2} \right)$$

else

$$\frac{1}{\mathrm{length}\left( y \right)} \cdot \mathrm{sum}\left( \left\|y - ŷ\right\| - 0.5 \right)$$

## …






























































