---
title: Phrase Representation Learning

tags: architecture 
---

# Phrase Representation Learning
- [Learning Phrase Representations Using RNN Encoder–Decoder for Statistical Machine Translation](https://www.aclweb.org/anthology/D14-1179/)
- two recurrent neural networks [Basic RNN Architectures](Basic%20RNN%20Architectures.md) that is together able to learn the mapping from a sequence of an arbitrary length to another sequence, possibly from a different set, of an arbitrary length.
- either score a pair of sequences (in terms of a conditional probability) or generate a target sequence given a source sequence
- jointly trained to maximize the conditional probability of a target sequence given a source sequence
- reset gate and an update gate that adaptively control how much each hidden unit remembers or forgets while reading/generating a sequenc
- RNN Encoder–Decoder to score each phrase pair in the phrase table
- capture linguistic regularities in the phrase pairs well
- [BLEU](BLEU.md)














