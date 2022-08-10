---
title: AutoEncoder
tags: architecture
date modified: Thursday, August 11th 2022, 12:32:57 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AutoEncoder
- ![im](assets/Pasted%20image%2020220310204652.png)
- Regression by predicting a reconstruction of the data
- Encoder $$E : \mathscr{X} \rightarrow \mathscr{F}$$
- Decoder $$\mathscr{F} \rightarrow \mathscr{D}$$
- $$E_\theta, D_\theta = argmin_{E_\theta, D\theta}||X-D(E(X))||^2$
	- Learn using [Gradient Descent gradients](Gradient%20Descent%20gradients.md)
- Compressed rep of data -> Good for Classification or Regression
- [MSE](MSE.md) : Unsupervised

## Difficulties
- dim $\mathscr{F} \lt \mathscr{X}$
	- Cannot learn the identity function
- usages
    - data compression / dimensionality reduction
    - encoder to obtain features (use the latent variable as feature)
    - denoising autoencoders
        - input noisy image and try to obtain image without noise
    - sparse auto-encoder
    - contractive autoencoder

## Types
- [Denoising Autoencoder](Denoising%20Autoencoder.md)
- [VAE](VAE.md)

