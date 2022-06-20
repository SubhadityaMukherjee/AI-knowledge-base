---
title: Imagen

tags: architecture 
---

# Imagen
- better top-1 accuracy on [ImageNet](ImageNet.md) than [EfficientNet](EfficientNet.md) at similar latency
- [Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding](https://arxiv.org/abs/2205.11487)
- text-to-image diffusion model
- large [Transformer](Transformer.md) language models in understanding text and hinges on the strength of diffusion models in high-fidelity image generation
- Imagen produces $1024 \times 1024$ samples with unprecedented photorealism and alignment with text
- generic large language models (e.g. T5), pretrained on text-only corpora, are surprisingly effective at encoding text for image synthesis
- increasing the size of the language model in Imagen boosts both sample fidelity and image-text alignment much more than increasing the size of the image diffusion model
- FID score
- [COCO](COCO.md)
- [[DrawBench]]
- With DrawBench, we compare Imagen with recent methods including [[VQGAN]]+[[CLIP]], [[Latent Diffusion]] Models, and [[DALL-E]], and find that human raters prefer Imagen over other models in side-by-side comparisons, both in terms of sample quality and image-text alignment








