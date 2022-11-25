---
title: Pruning
tags: regularize
date modified: Monday, October 10th 2022, 2:02:19 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Pruning
- Mainly that of being able to reduce the size, cost and computational requirements of my models, all while maintaning the accuracy (sort of atleast).
- Generally this comes about by removing parameters in some form or fashion.
- Rather than taking a mask, we can prune certain parts of the network by setting them to 0 or by dropping them if required. (aka weights and biases)
- In most cases, the network is first trained for a while. Then pruned. Which reduces its accuracy and is thus trained again (fine tuning). This cycle is repeated until we get the results we require.
- Major Types of Pruning Methods
- [Structure_Based_Pruning](Structure_Based_Pruning.md)
- [Scoring_Pruning_Approaches](Scoring_Pruning_Approaches.md)
- [Scheduling](Scheduling.md)
- [Fine_Tuning_Based_Pruning](Fine_Tuning_Based_Pruning.md)
- [Global_Magnitude_Based_Pruning](Global_Magnitude_Based_Pruning.md)
- [Global_Gradient_Magnitude_Based_Pruning](Global_Gradient_Magnitude_Based_Pruning.md)
- [Layerwise_Gradient_Magnitude_Based_Pruning](Layerwise_Gradient_Magnitude_Based_Pruning.md)
- [Random_Pruning](Random_Pruning.md)
- [Layerwise_Magnitude_Based_Pruning](Layerwise_Magnitude_Based_Pruning.md)

