---
tags: temp
title: Cosine Learning Rate Decay
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Cosine Learning Rate Decay
- Instead of [[Learning Rate Warmup]] and then decay
- $$\eta_{\mathrm{t}}=\frac{1}{2}\left(1+\cos\left(\frac{\mathrm{t}\pi}{\mathrm{\mathrm{T}}}\right)\right)\eta$$
- Rate decreases slowly at first, then almost linear in the middle and slows down again in the end
- ![[assets/Pasted image 20220502134254.png|im]]

## Backlinks
> - [Learning Rate Decay #tricks](Learning Rate Decay tricks.md)
>   - [[Cosine Learning Rate Decay]]

_Backlinks last generated 2022-10-04 13:01:19_
