---
toc: true
title: Textless Speech Emotion Conversion

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Textless Speech Emotion Conversion
- [Textless Speech Emotion Conversion Using Discrete and Decomposed Representations](https://arxiv.org/abs/2111.07402)
- Speech emotion conversion
- modifying the perceived emotion of a speech utterance while preserving the lexical content and speaker identity
- spoken language translation task
- decomposition of the speech signal into discrete learned representations, consisting of phonetic-content units, prosodic [Features](Features.md), speaker, and emotion
- modify the speech content by translating the phonetic-content units to a target emotion, and then predict the prosodic [Features](Features.md) based on these units
- speech waveform is generated by feeding the predicted representations into a neural vocoder
- beyond spectral and parametric changes of the signal
- model non-verbal vocalizations, such as laughter insertion, yawning removal, etc



