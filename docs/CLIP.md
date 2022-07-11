---
title: CLIP

tags: architecture 
---

# CLIP
- [Learning Transferable Visual Models from Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- introduces CLIP, a pre-training task which efficiently learns visual concepts from natural language supervision
- performs language-guided image generation
- uses vision and language encoders trained in isolation and uses a contrastive loss to bring similar image-text pairs closer, while pulling apart dissimilar pairs as a part of pretaining
- can be applied to any visual classification benchmark by simply providing the names of the visual categories to be recognized, similar to the “zero-shot” capabilities of [GPT](GPT.md) and [GPT3](GPT3.md)
- pre-trains an image encoder and a text encoder to predict which images were paired with which texts in our dataset
- zero-shot classifier
- they convert all of a dataset’s classes into captions such as “a photo of a dog” and predict the class of the caption CLIP estimates best pairs with a given image








