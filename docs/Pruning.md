---
title: Pruning
tags: regularize
---

# Pruning
- Mainly that of being able to reduce the size, cost and computational requirements of my models, all while maintaning the accuracy (sort of atleast). 
- Generally this comes about by removing parameters in some form or fashion. 
- Rather than taking a mask, we can prune certain parts of the network by setting them to 0 or by dropping them if required. (aka weights and biases)
- In most cases, the network is first trained for a while. Then pruned. Which reduces its accuracy and is thus trained again (fine tuning). This cycle is repeated until we get the results we require.
- Major Types of Pruning Methods

- [[Structure Based Pruning]]

- [[Scoring Pruning Approaches]]

- [[Scheduling]]

- [[Fine Tuning Based Pruning]]

- [[Global Magnitude Based Pruning]]

- [[Global Gradient Magnitude Based Pruning]]

- [[Layerwise Gradient Magnitude Based Pruning]]

- [[Random Pruning]]
- [[Layerwise Magnitude Based Pruning]]










