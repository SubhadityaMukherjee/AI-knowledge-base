---
title: VICReg

tags: architecture 
---
- [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](https://arxiv.org/abs/2105.04906)
- [Self Supervised](Self%20Supervised.md)
- based on maximizing the agreement between [Embedding](Embedding.md) vectors from different views of the same image
- rivial solution is obtained when the encoder outputs constant vectors
- [Mode Collapse](Mode%20Collapse.md) is often avoided through implicit biases
- explicitly avoids the collapse problem with a simple [regularization](Regularization.md) term on the variance of the embeddings along each dimension individually
- triple objective: learning invariance to different views with a invariance term, avoiding collapse of the representations with a variance preservation term, and maximizing the information content of the representation with a [covariance](Covariance.md) [regularization](Regularization.md) term
- [Bias Vs Variance](Bias%20Vs%20Variance)
- combines the variance term with a decorrelation mechanism based on redundancy reduction and [covariance](Covariance.md) [regularization](Regularization.md)
- does not require the [embedding](Embedding.md) branches to be identical or even similar
































































