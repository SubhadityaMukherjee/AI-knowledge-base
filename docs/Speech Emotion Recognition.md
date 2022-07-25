---
title: Speech Emotion Recognition

tags: architecture 
---

# Speech Emotion Recognition
- [GAN-based Data Generation for Speech Emotion Recognition](http://www.interspeech2020.org/uploadfile/pdf/Wed-3-10-12.pdf)
- form of speech emotion spectrograms
- used for training speech emotion recognition networks
- nvestigate the usage of GANs for capturing the data manifold when the data is eyes-off, i.e., where they can train networks using the data but cannot copy it from the clients
- CNN-based GAN with spectral normalization on both the generator and discriminator, both of which are pre-trained on large unlabeled speech corpora
- even after the data on the client is lost, their model can generate similar data that can be used for model bootstrapping in the future
















