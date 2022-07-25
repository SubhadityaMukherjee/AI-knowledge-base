---
title: Listen Attend Spell

tags: architecture 
---

# Listen Attend Spell
- [Listen, Attend and Spell](https://arxiv.org/abs/1508.01211)
- LAS
- learns to transcribe speech utterances to characters
- nlike traditional DNN-HMM models, this model learns all the components of a speech recognizer jointly
- sequence-to-sequence framework
- trained end-to-end and has two main components: a listener (encoder) and a speller (decoder)
- listener is a pyramidal RNN encoder that accepts filter bank spectra as inputs, transforms the input sequence into a high level feature representation and reduces the number of timesteps that the decoder has to attend to.
- The speller is an [attention](Attention.md)-based RNN decoder that attends to the high level [features](Features.md) and spells out the transcript one character at a time
- The proposed system does not use the concepts of phonemes, nor does it rely on pronunciation dictionaries or HMMs
- bypass the conditional independence assumptions of [CTC](CTC.md), and show how they can learn an implicit language model that can generate multiple spelling variants given the same acoustics
- producing character sequences without making any independence assumptions between the characters is the key improvement of LAS over previous end-to-end [CTC](CTC.md) models
- used samples from the [softmax](Softmax.md) classifier in the decoder as inputs to the next step prediction during training
- show how a language model trained on additional text can be used to rerank their top hypotheses
- [Google voice search task](Google%20voice%20search%20task.md)


















