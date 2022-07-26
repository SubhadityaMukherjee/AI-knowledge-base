---
title: wave2vec 2

tags: architecture 
---

# wave2vec 2
- [wav2vec 2.0: a Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477)
- earning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best semi-supervised methods while being conceptually simpler
- masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned
- Compared to wav2vec, wav2vec 2.0 learns basic speech units used to tackle a self-supervised task
- trained to predict the correct speech unit for masked parts of the audio, while at the same time learning what the speech units should be
- [[LibriSpeech]]
- feasibility of speech recognition with limited amounts of labeled data
- [[XLSR]]
- learn speech units common to several languages
- helps when they have even small amounts of unlabeled speech, since languages for which they have little data can benefit from languages for which more data is available






















