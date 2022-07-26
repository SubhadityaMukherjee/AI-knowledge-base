---
title: AutoEncoder
tags: architecture
---

# AutoEncoder
- ![[assets/Pasted image 20220310204652.png|im]]
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


































































































## Backlinks

> - [Unsupervised Learning](Unsupervised Learning.md)
>   - [[Auto Encoders]]
>    
> - [Masked Autoencoders](Masked Autoencoders.md)
>   - [[ImageNet]] and in [[Transfer Learning]] that an [[Auto Encoders]] —- a simple self-supervised method similar to techniques in NLP – provides scalable benefits

_Backlinks last generated 2022-07-26 20:33:15_
