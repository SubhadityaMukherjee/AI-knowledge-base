---
title: Mixed chunk attention

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Mixed Chunk [Attention](Attention.md)
- an efficient linear approximation method that combines the benefits from partial and linear [attention](Attention.md) mechanisms, which is accelerator-friendly and highly competitive in quality.
- The method works on chunks of tokens and leverages local (within chunk) and global (between chunks) [attention](Attention.md) spans

