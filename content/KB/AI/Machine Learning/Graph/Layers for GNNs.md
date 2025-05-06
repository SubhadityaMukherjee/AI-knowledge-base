---
title: Layers for GNNs
toc: true
tags:
  - graph
date modified: Wednesday 30th October 2024, Wed
date created: Wednesday 30th October 2024, Wed
---

# Layers for GNNs
```toc
```

## Layers for GNNs
- combined messages from adjacent nodes by summing them together with the transformed current node -> post-multiplying the node embedding matrix H by the adjacency matrix plus the identity A + I
### Combining Current Node and Aggregated Neighbors
- ![[Pasted image 20241030115325.png]]

### Residual Connections
- ![[Pasted image 20241030112449.png]]

### Mean Aggregation
- Sometimes it's better to take the average of the neighbors rather than the sum; this can be superior if the embedding information is more important and the structural information less so since the magnitude of the neighborhood contributions will not depend on the number of neighbors
- ![[Pasted image 20241030114702.png]]
- ![[Pasted image 20241030112531.png]]
 
### [[Kipf Normalization]]

### Max Pooling Aggregation
- ![[Pasted image 20241030112617.png]]

### Aggregation by Attention
- ![[Pasted image 20241030114716.png]]
- ![[Pasted image 20241030112650.png]]
- similar to [[Self Attention]] 
- ![[Pasted image 20241030112709.png]]
- ![[Pasted image 20241030112804.png]]
