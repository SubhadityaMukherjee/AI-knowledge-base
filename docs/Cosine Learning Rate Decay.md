---
tags: temp
title: Cosine Learning Rate Decay
date modified: Wednesday, August 10th 2022, 11:41:30 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cosine Learning Rate Decay
- Instead of [Learning Rate Warmup](Learning%20Rate%20Warmup.md) and then decay
- $$\eta_{\mathrm{t}}=\frac{1}{2}\left(1+\cos\left(\frac{\mathrm{t}\pi}{\mathrm{\mathrm{T}}}\right)\right)\eta$$
- Rate decreases slowly at first, then almost linear in the middle and slows down again in the end
- ![im](assets/Pasted%20image%2020220502134254.png)

