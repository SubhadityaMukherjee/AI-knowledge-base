---
title: Variational Autoencoder
tags: architecture 
---

# Variational Autoencoder
- Some control over distribution of learned [[Features|features]]
- Eg: Decoder as a generative model
- Constraint loss function and a given [[Probability]] $\mathcal{D}$
	- Eg: By Loss func [[KL Divergence]] and prob distribution $$L(X) = n^{-1}\Sigma_i||x_i - D(E(\tilde x))||^2 + \lambda \cdot KL(f_i, d)$$
	- Use 2D unit distribution. 0 mean, unit variance
	- Latent vector : $$f=\mu + \epsilon e^{2log\sigma}$$
- $$L(X) = n^{-1}\Sigma_i||x_i - D(E(\tilde x))||^2 + \frac{1}{2n}\Sigma_i(e^{log\sigma(x_i)} + \mu(x_i)^2 -1 -log(\sigma (x_i))$$
- Encoder predicts mean and std $$E(x_i) = (\mu(x_i) , log \sigma(x_i))$$


































































































## Backlinks

> - [AutoEncoder](Auto Encoders.md)
>   - [[VAE]]
>    
> - [BEiT](BEiT.md)
>   - discrete [[VAE]] (dVAE) which acts as an “image [[Tokenizer|tokenizer]]” learnt via autoencoding-style reconstruction
>   - input image is tokenized into discrete visual tokens obtained by the latent codes of the discrete [[VAE]]

_Backlinks last generated 2022-07-26 20:33:15_
