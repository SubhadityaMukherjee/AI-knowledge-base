---
title: DALL-E 2

tags: architecture 
---

# DALL-E 2
- [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://cdn.openai.com/papers/dall-e-2.pdf)
- DALL-E 2, generates more realistic and accurate images with 4x greater resolution, better caption matching and photorealism
- Contrastive models like CLIP have been shown to learn robust representations of images that capture both semantics and style
- two-stage model: a prior that generates a CLIP image [embedding](Embedding.md) given a text caption, and a “unCLIP” decoder that generates an image conditioned on the image [embedding](Embedding.md)
- explicitly generating image representations improves image diversity with minimal loss in photorealism and caption similarity
- decoder, which is conditioned on image representations, can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation
- diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples





