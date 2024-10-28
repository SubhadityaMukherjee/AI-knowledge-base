---
title: Graph convolutional network
toc: true
tags:
  - architecture
  - graph
date modified: Tuesday 22nd October 2024, Tue
date created: Tuesday 22nd October 2024, Tue
---

# Graph Convolutional Network
```toc
```
- spatial-based convolutional graph neural networks, or GCNs
- These models are convolutional in that they update each node by aggregating information from nearby nodes
- [[relational inductive bias]]
- ![[Pasted image 20241022131105.png]]
  
## Equivariance and Invariance for Graphs
- if we permute the node indices, the node embeddings at each stage will be permuted in the same way.
- ![[Pasted image 20241022131324.png]]

## Parameter Sharing for Graphs

- We could learn a model with separate parameters associated with each node. However, now the network must independently learn the meaning of the connections in the graph at each position, and training would require many graphs with the same topology. 
- Instead, we build a model that uses the same parameters at every node, reducing the number of parameters and sharing what the network learns at each node across the entire graph
- One way to think of this is that each neighbor sends a message to the variable of interest, which aggregates these messages to form the update.
- ![[Pasted image 20241022131449.png]]

## Example GCN Layer
- ![[Pasted image 20241023120909.png]]
- ![[Pasted image 20241023120915.png]]
- this is equivariant, can cope with any number of neighbors, uses the graph srtucture to provide a [[Relational Inductive Bias]] and parameter sharing 

### Example : Graph Classification
- Network to classify molecules as harmless or toxic
- [[Adjacency matrix]] - $$A \in \mathbb{R}^{N \times N}$$
- Node embedding matrix - $$X \in \mathbb{R}^{118 \times N}$$
	- 118 elements of the periodic table
	- vectors of length 118 where every position is zero except for the position corresponding to the relevant element, which is set to one
- ![[Pasted image 20241023121234.png]]

### Example : Node Classification
- 
## Batching for GNN
- GIven I training graphs ${X_{i}, A_{i}}$ and labels $y_{i}$, params ${\Phi = \{\beta_{k}, \Omega_{k}}\}^{K}_{k=0}$ , [[SGD]]and [[Binary Cross Entropy]]
- We cannot concat batches into a big tensor since each graph has a different number of nodes
- Instead, we treat the graphs in each batch as disjoint components of a single large graph.
- we can then just run the network over this big graph as a single instance of the network equations.
- Then we can do mean pooling on it

## Inductive Models
- we exploit a training set of labeled data to learn the relation between the inputs and outputs.
-  Then we apply this to new test data. One way to think of this is that we are learning the rule that maps inputs to outputs and then applying it elsewhere.

## Transductive Models
- considers both the labeled and unlabeled data at the same time
- [[Semi Supervised]]
- It does not produce a rule but merely a labeling for the unknown outputs
- However, it has the disadvantage that the model needs to be retrained when extra unlabeled data are added.
