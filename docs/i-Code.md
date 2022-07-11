---
title: i-Code

tags: architecture 
---

# i-Code
- [i-Code: an Integrative and Composable Multimodal Learning Framework](https://arxiv.org/abs/2205.01818)
- Human intelligence is multimodal; they integrate visual, linguistic, and acoustic signals to maintain a holistic worldview
- Most current pretraining methods, however, are limited to one or two modalities.
- jointly learns representations for vision, language and speech into a unified, shared and general-purpose vector representation
- data from each modality are first given to pretrained single-modality encoder
- The encoder outputs are then integrated with a multimodal fusion network, which uses novel attention mechanisms and other architectural innovations to effectively combine information from the different modalities
- new objectives including (i) masked modality modeling and (ii) cross-modality contrastive learning
- pretraining on dual-modality datasets can also yield competitive or even better performance than pretraining on videos, the data resource that previous three-modality models were restricted to
- dynamically process single, dual, and triple-modality data during training and inference, flexibly projecting different combinations of modalities into a single representation space
- GLUE
- merge-attention layers and (b) co-attention layers
- fusion architecture
- mechanisms that merge and cross the attention scores of different modalities, namely merge-attention (based on self-attention) and co-attention (based on self- and cross-attention) respectively


## Backlinks

> - [](journals/2022-07-11.md)
>   - [[i-Code]]

_Backlinks last generated 2022-07-11 15:15:43_
