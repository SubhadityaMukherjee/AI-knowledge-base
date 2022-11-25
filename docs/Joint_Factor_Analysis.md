---
title: Joint Factor Analysis

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Joint Factor Analysis
- [Front-end Factor Analysis for Speaker Verification](http://groups.csail.mit.edu/sls/publications/2010/Dehak_IEEE_Transactions.pdf)
- Joint Factor Analysis (JFA)
- eature extractor to learn a low-dimensional speaker representation for [speaker verification](Speaker_Verification.md), which is also used to model session and channel effects/variabilities
- In this new space, a given speech utterance is represented by a new vector named total factors (called the identity-vector or the “i-vector”)
- The i-vector is thus a feature that represents the characteristics of the frame-level [features](Features.md)’ distributive pattern
- dimensionality reduction of the GMM supervector (although the GMM supervector is not extracted when computing the i-vector)
- extracted in a similar manner with the eigenvoice adaptation scheme or the JFA technique
- extracted per sentence
- Support-Vector-Machine-based system that uses the cosine kernel to estimate the similarity between the input data
- [cosine similarity](Cosine_Similarity.md) as the final decision score
- removed the SVM from the decision proces
- no speaker enrollment
- EER
- MinDCF
- [NIST_2008_Speaker_Recognition_Evaluation_dataset](NIST_2008_Speaker_Recognition_Evaluation_dataset.md)
- Up until d-vectors, the state-of-the-art [speaker verification](Speaker_Verification.md) systems were based on the concept of i-vectors

