---
title: GE2E

tags: loss 
---

# GE2E
- [Generalized End-to-end Loss for Speaker Verification](https://arxiv.org/abs/1710.10467)
- new loss function
- training of [[Speaker Verification|speaker verification]] models more efficient
- Unlike TE2E, the GE2E loss function updates the network in a way that emphasizes examples that are difficult to verify at each step of the training process
- pushes the [[Embedding|embedding]] towards the centroid of the true speaker, and away from the centroid of the most similar different speaker
- does not require an initial stage of example selection
- [[MultiReader technique]]






















