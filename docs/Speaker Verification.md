---
title: Speaker Verification

tags: architecture 
---

# Speaker Verification
- [Deep Neural Networks for Small Footprint Text-dependent Speaker Verification](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41939.pdf)
- nvestigates the use of deep neural networks (DNNs) to train speaker embeddings for a small footprint text-dependent speaker verification task
- stacked filterbank [features](Features.md) as input
- During speaker enrollment, the trained DNN is used to extract speaker-specific [features](Features.md)/embeddings by averaging the activations from the last hidden layer (called deep-vectors or “d-vectors” for short), which is taken as the speaker model
- d-vector is extracted for each utterance and compared to the enrolled speaker model to make a verification decision by calculating the cosine distance between the test d-vector and the claimed speaker’s d-vector, similar to the i-vector framework
- A verification decision is made by comparing the distance to a threshold
- DNN based speaker verification system achieves good performance compared to a popular i-vector system on a small footprint text-dependent speaker verification task






















