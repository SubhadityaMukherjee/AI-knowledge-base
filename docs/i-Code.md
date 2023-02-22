---
title: i-Code

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:12 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# i-Code
- [i-Code: an Integrative and Composable Multimodal Learning Framework](https://arxiv.org/abs/2205.01818)
- Human intelligence is multimodal; they integrate visual, linguistic, and acoustic signals to maintain a holistic worldview
- Most current pretraining methods, however, are limited to one or two modalities.
- jointly learns representations for vision, language and speech into a unified, shared and general-purpose vector representation
- data from each [[modality]] are first given to pretrained single-[[modality]] encoder
- The encoder outputs are then integrated with a multimodal fusion network, which uses novel [attention](Attention.md) mechanisms and other architectural innovations to effectively combine information from the different modalities
- new objectives including (i) masked [[modality]] modeling and (ii) cross-[[modality]] contrastive learning
- pretraining on dual-[[modality]] datasets can also yield competitive or even better performance than pretraining on videos, the data resource that previous three-[[modality]] models were restricted to
- dynamically process single, dual, and triple-[[modality]] data during training and inference, flexibly projecting different combinations of modalities into a single representation space
- [GLUE](GLUE.md)
- merge-attention [layers](Layers.md) and (b) co-[attention](Attention.md) [layers](Layers.md)
- fusion architecture
- mechanisms that merge and cross the [attention](Attention.md) scores of different modalities, namely merge-[attention](Attention.md) (based on self-[attention](Attention.md)) and co-[attention](Attention.md) (based on self- and cross-[attention](Attention.md)) respectively

