---
title: Flamingo

tags: architecture 
---

# Flamingo
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- large-scale pre-training followed by task-specific fine-tuning has emerged as a standard approach, but the fine-tuning step still requires a lot of samples.
- building models that can be rapidly adapted to numerous tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research
- family of Visual Language Models (VLM) which seek to train a multi-modal model (i.e., with the ability to understand different types of input – visual, audio, text etc.) in a few-shot learning approach (which refers to the ability to learn a new task with just a few samples for training).
- bridge powerful pretrained vision-only and language-only models
- handle sequences of arbitrarily interleaved visual and textual data
- seamlessly ingest images or videos as inputs
- Interleave cross-attention layers with language-only self-attention layers (frozen).
- Perceiver-based architecture that transforms the input sequence data (videos) into a fixed number of visual token
- Large-scale (web) multi-modal data by scraping webpages which has inter-leaved text and images
- Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities




