---
title: Neural Probabilistic Model

tags: architecture 
---

# Neural Probabilistic Model
- [A Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)
- more compact and smoother representations based on distributed representations that can accommodate far more conditioning variables
- learning the joint [probability](Probability.md) function of sequences of words in a language was intrinsically difficult because of the curse of dimensionality
- learning a distributed representation for words which allows each training sentence to inform the model about an exponential/combinatorial number of semantically neighboring sentences
- The model learns simultaneously (i) a distributed representation for each word along with (ii) the [probability](Probability.md) function for word sequences, expressed in terms of these representations
- Generalization is obtained because a sequence of words that has never been seen before gets high [probability](Probability.md) if it is made of words that are similar
- significantly improves on state-of-the-art [[n gram]] models








































