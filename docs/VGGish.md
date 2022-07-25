---
title: VGGish

tags: architecture 
---

# VGGish
- [CNN Architectures for Large-Scale Audio Classification](https://arxiv.org/abs/1609.09430)
- applying various state-of-the-art image networks with CNN architectures to audio and show that they are capable of excellent results on audio classification
- examine fully connected deep neural networks such as AlexNet, VGG, InceptionNet, and ResNet
- The input audio is divided into non-overlapping 960 ms frames which are decomposed by applying the Fourier transform, resulting in a spectrogram
- spectrogram is integrated into 64 mel-spaced frequency bins, and the magnitude of each bin is log-transformed
- gives log-mel spectrogram patches that are passed on as input to all classifiers
- Acoustic Event Detection
- train a classifier on embeddings learned from the video-level task on AudioSet
- model for AED with embeddings learned from these classifiers does much better than raw [features](Features.md) on the Audio Set AED classification task
- derivatives of image classification networks do well on the audio classification task
- increasing the number of labels they train on provides some improved performance over subsets of labels
- performance of models improves as they increase training set size,
- model using embeddings learned from the video-level task do much better than a baseline on the [[AudioSet classification]] task
















