---
title: GloVE

tags: architecture 
---

# GloVE
- [GloVe: Global Vectors for Word Representation](https://www.aclweb.org/anthology/D14-1162/)
- [Word2Vec](Word2Vec.md) relies only on local information of language. That is, the semantics learnt for a given word, is only affected by the surrounding words.
- [Unsupervised Learning](Unsupervised%20Learning.md) algorithm which captures both global statistics and local statistics of a corpus
- aggregated global word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space
- whether distributional word representations are best learned from count-based methods or from prediction-based methods
- probe the underlying co-occurrence statistics of the corpus
- reformulated word2vec optimizations as a special kind of factorization for word co-occurence matrices
- Note that GloVe does not use neural networks
- utilizes this main benefit of count data while simultaneously capturing the meaningful linear substructures prevalent in recent log-bilinear prediction-based methods like word2vec
- global log-bilinear [LinearRegression](LinearRegression.md) model for the unsupervised learning of word representations












