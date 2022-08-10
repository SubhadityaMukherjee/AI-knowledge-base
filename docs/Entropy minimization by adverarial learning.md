---
title: Entropy minimization by adverarial learning

tags: temp
date modified: Wednesday, August 10th 2022, 11:41:29 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Entropy Minimization by Adverarial Learning
- A limitation of the entropy loss is related to the absence of structural dependencies between local semantics.
- This is caused by the aggregation of the pixel-wise prediction entropies by summation.
- unified adversarial training framework which minimizes indirectly the entropy of target data, by encouraging it to become similar to the source one.
- minimizing distribution distance between source and target on the weighted self-information space
- We perform the adversarial adaptation on weighted self-information maps using a fully-convolutional discriminator network
- the discriminator produces domain classification outputs, i.e., class label for the source (resp. target) domain.
- discriminate outputs coming from source and target images, and at the same time, train the segmentation network to fool the discriminator.

