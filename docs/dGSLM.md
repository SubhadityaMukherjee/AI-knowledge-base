---
title: dGSLM

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:43 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# dGSLM
- [Generative Spoken Dialogue Language Modeling](https://arxiv.org/abs/2203.16502)
- dGSLM
- first “textless” model able to generate audio samples of naturalistic spoken dialogues
- unsupervised spoken unit discovery coupled with a dual-tower [transformer](Transformer.md) architecture with cross-[attention](Attention.md) trained on 2000 hours of two-channel raw conversational audio [Fisher Spanish-English](Fisher%20Spanish-English.md) without any text or labels
- generate speech, laughter and other paralinguistic signals in the two channels simultaneously and reproduces naturalistic turn taking

