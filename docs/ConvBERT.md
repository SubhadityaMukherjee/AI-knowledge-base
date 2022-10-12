---
title: ConvBERT

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# ConvBERT
- Convolutional BERT (ConvBERT) improves the original [[BERT]] by replacing some [[Multi Head Attention]] [[Self Attention]] segments with cheaper and naturally local operations, so-called [[span-based dynamic convolutions]]. These are integrated into the self-[[Attention|attention]] mechanism to form a mixed [[Attention|attention]] mechanism, allowing Multi-headed Self-[[Attention|attention]] to capture global patterns; the Convolutions focus more on the local patterns, which are otherwise captured anyway. In other words, they reduce the computational intensity of training BERT.

