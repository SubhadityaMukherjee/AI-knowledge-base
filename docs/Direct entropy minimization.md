---
title: Direct entropy minimization

tags: 
---

# Direct Entropy Minimization
 - On the source domain we train our model,
- as usual using a supervised loss
- For the target domain, we do not have annotations and we can no longer use the segmentation loss to train
- supervision signal that could leverage visual information from the target samples, in spite of the lack of annotations
- constrain
- to produce high-confident predictions on target samples similarly to source samples
- entropy loss $\mathcal{L}_{ent}$ to maximize directly the prediction confidence in the target domain.
- [Shannon Entropy](Shannon%20Entropy)






































