---
title: Cosine Learning Rate Decay
---

# Cosine Learning Rate Decay
- Instead of [[Learning Rate Warmup]] and then decay
- $$\eta_{\mathrm{t}}=\frac{1}{2}\left(1+\cos\left(\frac{\mathrm{t}\pi}{\mathrm{\mathrm{T}}}\right)\right)\eta$$
- Rate decreases slowly at first, then almost linear in the middle and slows down again in the end
- ![[9F2A509E-5D9B-489A-9210-097C8746CC8B.jpeg]]


