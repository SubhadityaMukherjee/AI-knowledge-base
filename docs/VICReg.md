---
title: VICReg

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:14 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---
- [VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning](https://arxiv.org/abs/2105.04906)
- [[Self Supervised]]
- based on maximizing the agreement between [[Embedding]] vectors from different views of the same image
- rivial solution is obtained when the encoder outputs constant vectors
- [[Mode Collapse]] is often avoided through implicit biases
- explicitly avoids the collapse problem with a simple [[Regularization|regularization]] term on the variance of the embeddings along each dimension individually
- triple objective: learning invariance to different views with a invariance term, avoiding collapse of the representations with a variance preservation term, and maximizing the information content of the representation with a [[Covariance|covariance]] [[Regularization|regularization]] term
- [[Bias Vs Variance]]
- combines the variance term with a decorrelation mechanism based on redundancy reduction and [[Covariance|covariance]] [[Regularization|regularization]]
- does not require the [[Embedding|embedding]] branches to be identical or even similar

