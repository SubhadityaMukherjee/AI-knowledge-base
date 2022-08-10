---
title: Mixed chunk attention

tags: architecture 
date modified: Wednesday, August 10th 2022, 11:41:26 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Mixed Chunk [Attention](Attention.md)
- an efficient linear approximation method that combines the benefits from partial and linear [attention](Attention.md) mechanisms, which is accelerator-friendly and highly competitive in quality.
- The method works on chunks of tokens and leverages local (within chunk) and global (between chunks) [attention](Attention.md) spans

