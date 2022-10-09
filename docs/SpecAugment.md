---
title: SpecAugment

tags: augment 
date modified: Friday, October 7th 2022, 12:18:59 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# SpecAugment
- [SpecAugment: a Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779)
- simple data [[Augmentation|augmentation]] method for speech recognition
- applied directly to the feature inputs of a neural network
- warping the [[Features|features]], masking blocks of frequency channels, and masking blocks of time steps
- apply SpecAugment on Listen, Attend and Spell (LAS) networks for end-to-end speech recognition tasks
- [[LibriSpeech]]
- [[Swichboard]]
- end-to-end LAS networks by augmenting the training set using simple handcrafted policies
- converts ASR from an over-[[Fitting|fitting]] to an under-[[Fitting|fitting]] problem, and they are able to gain performance by using bigger networks and training longer

