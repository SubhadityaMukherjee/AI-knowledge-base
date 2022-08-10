---
title: SpecAugment

tags: regularize 
date modified: Wednesday, August 10th 2022, 11:41:23 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# SpecAugment
- [SpecAugment: a Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779)
- simple data [augmentation](Augmentation.md) method for speech recognition
- applied directly to the feature inputs of a neural network
- warping the [features](Features.md), masking blocks of frequency channels, and masking blocks of time steps
- apply SpecAugment on Listen, Attend and Spell (LAS) networks for end-to-end speech recognition tasks
- [LibriSpeech](LibriSpeech.md)
- [Swichboard](Swichboard.md)
- end-to-end LAS networks by augmenting the training set using simple handcrafted policies
- converts ASR from an over-[fitting](Fitting.md) to an under-[fitting](Fitting.md) problem, and they are able to gain performance by using bigger networks and training longer

