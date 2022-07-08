---
title: Speech Recognition

tags: architecture 
---

# Speech Recognition
- [Recurrent Neural Network Based Language Model](https://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf)
	- 50% reduction of [[Perplexity]]
	- mixture of several [Basic RNN Architectures](Basic%20RNN%20Architectures.md)
	- [[Wall Street Journal task]]
	- connectionist language models are superior to standard [n gram](n%20gram) techniques, except their high computational (training) complexity
	- break the myth that language modeling is just about counting n-grams, and that the only reasonable way how to improve results is by acquiring new training dat
- [Towards End-To-End Speech Recognition with Recurrent Neural Networks](http://proceedings.mlr.press/v32/graves14.pdf)
	- character-level speech recognition system that directly transcribes audio data with text using a recurrent neural network
	- combination of the deep bidirectional LSTM recurrent neural network architecture and a modified Connectionist Temporal Classification ([CTC](CTC.md)) objective function
	- word error rate
	- [Wall Street Journal task](Wall%20Street%20Journal%20task.md)








