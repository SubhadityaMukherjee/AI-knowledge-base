---
title: Operator Fusion
tags: parallel
date modified: Thursday, August 11th 2022, 12:32:49 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Operator Fusion
- Some DirectML operators support a concept known as _fusion_. Operator fusion is a way to improve performance by merging one operator (typically, an activation function) into a different operator so that they are executed together without requiring a roundtrip to memory.
- <https://arxiv.org/abs/2108.13342>

