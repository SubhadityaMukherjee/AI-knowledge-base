---
title: Joint Factor Analysis

tags: architecture 
---

# Joint Factor Analysis
- [Front-end Factor Analysis for Speaker Verification](http://groups.csail.mit.edu/sls/publications/2010/Dehak_IEEE_Transactions.pdf)
- Joint Factor Analysis (JFA)
- eature extractor to learn a low-dimensional speaker representation for [speaker verification](Speaker%20Verification.md), which is also used to model session and channel effects/variabilities
- In this new space, a given speech utterance is represented by a new vector named total factors (called the identity-vector or the “i-vector”)
- The i-vector is thus a feature that represents the characteristics of the frame-level [features](Features.md)’ distributive pattern
- dimensionality reduction of the GMM supervector (although the GMM supervector is not extracted when computing the i-vector)
- extracted in a similar manner with the eigenvoice adaptation scheme or the JFA technique
- extracted per sentence
- Support-Vector-Machine-based system that uses the cosine kernel to estimate the similarity between the input data
- [cosine similarity](Cosine%20Similarity.md) as the final decision score
- removed the SVM from the decision proces
- no speaker enrollment
- EER
- MinDCF
- [[NIST 2008 Speaker Recognition Evaluation dataset]]
- Up until d-vectors, the state-of-the-art [speaker verification](Speaker%20Verification.md) systems were based on the concept of i-vectors














