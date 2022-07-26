---
title: Google NMT

tags: architecture 
---

# Google NMT
- [Google’s Neural Machine Translation System: Bridging the Gap Between Human and Machine Translation](https://arxiv.org/abs/1609.08144)
	- deep [[LSTM)](Long Short Term Memory (LSTM|Long Short Term Memory (LSTM)]].md) network with 8 encoder and 8 decoder [[Layers|layers]] using [[Attention|attention]] and residual connections
	- improve parallelism and therefore decrease training time, their [[Attention|attention]] mechanism connects the bottom layer of the decoder to the top layer of the encoder
	- low-precision arithmetic during inference computations ([[FP16 training]] ???)
	- improve handling of rare words, we divide words into a limited set of common sub-word units
	- good balance between the flexibility of “character”-delimited models and the efficiency of “word”-delimited models
	- [[Beam search]] technique employs a length-normalization procedure and uses a coverage penalty




































































