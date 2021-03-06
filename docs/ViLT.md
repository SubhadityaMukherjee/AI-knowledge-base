---
title: ViLT

tags: architecture 
---

# ViLT
- [ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision](https://arxiv.org/abs/2102.03334)
- Vision-and-Language Transformer
- seeks to improve performance on various joint vision-and-language downstream tasks
- Current approaches to VLP heavily rely on image feature extraction processes using convolutional visual [embedding](Embedding.md) networks (e.g., Faster R-CNN and ResNets), which involve region supervision (e.g., object detection) and the convolutional architecture (e.g., ResNet)
- This is problematic in terms of both efficiency/speed, in that extracting input [features](Features.md) requires much more computation than the multimodal interaction steps; and expressive power, as it is upper bounded to the expressive power of the visual embedder and its predefined visual vocabulary.
- minimal VLP model, which is monolithic in that the processing of visual inputs is drastically simplified to just the same convolution-free manner that they process textual inputs
- removing the need for object detectors
- avoiding heavyweight image encoders by directly [embedding](Embedding.md) low-level pixel data with a single-layer projection and achieves similar results with reduced complexity,
- Self-supervision is accomplished using (i) Image Text Matching (ITM) loss and (ii) Masked Language Model (MLM) loss
- [[ITM Loss]]
- For text, ViLT simply reuses Masked Language Model - (MLM), used in BERT.
- [[MSCOCO]]
- [[Visual Genome]]
- [[SBU Captions]]
- [[Google Conceptual Captions]]
- [[VQAv2]]
- [[NLVR2]]
- [[Flickr30K]]
- ViLT is over 10x faster than previous VLP models, yet with competitive or better downstream task performance
- VLP needs to focus more on the multi-modality interactions aspect inside the transformer module rather than engaging in an arms race that merely powers up unimodal embedders








