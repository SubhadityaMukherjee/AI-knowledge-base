---
title: GloVE

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GloVE
- [GloVe: Global Vectors for Word Representation](https://www.aclweb.org/anthology/D14-1162/)
- [[Word2Vec]] relies only on local information of language. That is, the semantics learnt for a given word, is only affected by the surrounding words.
- [[Unsupervised Learning]] algorithm which captures both global statistics and local statistics of a corpus
- aggregated global word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space
- whether distributional word representations are best learned from count-based methods or from prediction-based methods
- probe the underlying co-occurrence statistics of the corpus
- reformulated [[Word2Vec|word2vec]] optimizations as a special kind of factorization for word co-occurence matrices
- Note that GloVe does not use neural networks
- utilizes this main benefit of count data while simultaneously capturing the meaningful linear substructures prevalent in recent log-bilinear prediction-based methods like [[Word2Vec|word2vec]]
- global log-bilinear [[LinearRegression]] model for the [[Unsupervised Learning|unsupervised learning]] of word representations

