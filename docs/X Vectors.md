---
title: X Vectors

tags: architecture 
---

# X Vectors
- [X-Vectors: Robust DNN Embeddings for Speaker Recognition](https://www.danielpovey.com/files/2018_icassp_xvectors.pdf)
- data [[Augmentation|augmentation]] to improve performance of deep neural network (DNN) embeddings for speaker recognition
- trained to discriminate between speakers, maps variable-length utterances to fixed-dimensional embeddings called x-vectors
- prior studies have found that embeddings leverage large-scale training datasets better than i-vectors, it can be challenging to collect substantial quantities of labeled data for training
- use data [[Augmentation|augmentation]], consisting of added noise and reverberation, as an inexpensive method to multiply the amount of training data and improve robustness
- Their data [[Augmentation|augmentation]] strategy employs additive noises and reverberation
- Reverberation involves convolving room impulse responses (RIR) with audio
- simulated RIRs described by [Ko et al.](https://danielpovey.com/files/2017_icassp_reverberation.pdf)
- reverberation itself is performed with the multicondition training tools in the Kaldi ASpIRE recipe
- For additive noise, they use the [[MUSAN]] dataset, 
- PLDA classifier is used in the x-vector framework to make the final decision, similar to i-vector systems
- x-vectors are compared with i-vector baselines on [[Speakers in the Wild]] and [[NIST SRE 2016 Cantonese]] where they achieve superior performance on the evaluation datasets






















