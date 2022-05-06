---
title: AutoEncoder
tags: architecture
---

# AutoEncoder
- ![[Pasted image 20220310204652.png]]
- Regression by predicting a reconstruction of the data
- Encoder $$E : \mathscr{X} \rightarrow \mathscr{F}$$
- Decoder $$\mathscr{F} \rightarrow \mathscr{D}$$
- $$E_\theta, D_\theta = argmin_{E_\theta, D\theta}||X-D(E(X))||^2$$
	- Learn using [[Gradient Descent gradients]]
- Compressed rep of data -> Good for Classification or Regression
- [[MSE]] : Unsupervised

## Difficulties
- dim $\mathscr{F} \lt \mathscr{X}$
	- Cannot learn the identity function

## Types
- [[Denoising Autoencoder]]
- [[VAE]]












