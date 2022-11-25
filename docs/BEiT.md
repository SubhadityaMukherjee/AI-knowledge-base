---
tags: temp
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: BEiT

tags: architecture

---

# BEiT
- [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254)
	- [Self_Supervised](Self_Supervised.md) pre-trained representation model
	- Bidirectional [Encoder_Decoder_Attention](Encoder_Decoder_Attention.md) representations from [Vision_Transformer](Vision_Transformer.md)
	- masked image modeling task to pretrain vision Transformers
	- each image has two views in their pre-training
	- the embeddings of which are calculated as linear projections of flattened patches
	- visual tokens
	- discrete [VAE](VAE.md) (dVAE) which acts as an “image [tokenizer](Tokenizer.md)” learnt via autoencoding-style reconstruction
	- input image is tokenized into discrete visual tokens obtained by the latent codes of the discrete [VAE](VAE.md)
	- proposed method is critical to make [BERT](BERT.md) like pre-training (i.e., auto-encoding with masked input) work well for image Transformers
	- automatically acquired knowledge about semantic regions, without using any human-annotated data
	- randomly masks some image patches and feeds them into the backbone [Transformer](Transformer.md)
	- pre-training objective is to recover the original visual tokens based on the corrupted image patches
	- directly fine-tune the model parameters on downstream tasks by appending task [layers](Layers.md) upon the pretrained encoder
	- [ImageNet](ImageNet.md)
	- outperforming from-scratch [DeiT](DeiT.md)

