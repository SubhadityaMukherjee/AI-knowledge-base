---
categories: ['temp']
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

toc: true
title: BEiT

categories: ['temp']

---

# BEiT
- [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254)
	- [[Self Supervised.md|Self Supervised]] pre-trained representation model
	- Bidirectional [[Encoder Decoder Attention.md|Encoder Decoder Attention]] representations from [[Vision Transformer.md|Vision Transformer]]
	- masked image modeling task to pretrain vision Transformers
	- each image has two views in their pre-training
	- the embeddings of which are calculated as linear projections of flattened patches
	- visual tokens
	- discrete [[VAE.md|VAE]] (dVAE) which acts as an “image [[Tokenizer.md|tokenizer]]” learnt via autoencoding-style reconstruction
	- input image is tokenized into discrete visual tokens obtained by the latent codes of the discrete [[VAE.md|VAE]]
	- proposed method is critical to make [[BERT.md|BERT]] like pre-training (i.e., auto-encoding with masked input) work well for image Transformers
	- automatically acquired knowledge about semantic regions, without using any human-annotated data
	- randomly masks some image patches and feeds them into the backbone [[Transformer.md|Transformer]]
	- pre-training objective is to recover the original visual tokens based on the corrupted image patches
	- directly fine-tune the model parameters on downstream tasks by appending task [[Layers.md|layers]] upon the pretrained encoder
	- [[ImageNet.md|ImageNet]]
	- outperforming from-scratch [[DeiT.md|DeiT]]



