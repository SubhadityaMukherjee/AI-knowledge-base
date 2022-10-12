---
title: CLIP

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:32 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# CLIP
- [Learning Transferable Visual Models from Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- introduces CLIP, a pre-training task which efficiently learns visual concepts from natural language supervision
- performs language-guided image generation
- uses vision and language encoders trained in isolation and uses a [[Contrastive Loss|contrastive loss]] to bring similar image-text pairs closer, while pulling apart dissimilar pairs as a part of pretaining
- can be applied to any visual classification benchmark by simply providing the names of the visual categories to be recognized, similar to the “zero-shot” capabilities of [[GPT]] and [[GPT3]]
- pre-trains an image encoder and a text encoder to predict which images were paired with which texts in our dataset
- zero-shot classifier
- they convert all of a dataset’s classes into captions such as “a photo of a dog” and predict the class of the caption CLIP estimates best pairs with a given image

## Backlinks
> - [Imagen](Imagen.md)
>   - With [[DrawBench]], we compare Imagen with recent methods including [[VQGAN]]+[[CLIP]], [[Latent Diffusion]] Models, and [[DALL-E]], and find that human raters prefer Imagen over other models in side-by-side comparisons, both in terms of sample quality and image-text alignment
>
> - [[[DALL-E]] 2](DALL-E 2.md)
>   - Contrastive models like [[CLIP]] have been shown to learn robust representations of images that capture both semantics and style
>   - two-stage model: a prior that generates a [[CLIP]] image [[Embedding|embedding]] given a text caption, and a “unCLIP” decoder that generates an image conditioned on the image [[Embedding|embedding]]

_Backlinks last generated 2022-10-04 13:01:19_
