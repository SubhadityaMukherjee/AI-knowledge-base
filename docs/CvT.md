
---

title: CvT

tags: architecture 

---

# CvT
- [CvT: Introducing Convolutions to Vision Transformers](https://arxiv.org/abs/2103.15808)
	- improves [[Vision Transformer]]
	- introducing [[Conv]]
	- a hierarchy of Transformers containing a new convolutional token [[Embedding]]
	- convolutional Transformer block leveraging a convolutional projection
	- shift, scale, and distortion invariance
	- dynamic [[Attention]] , global context, and better generalization
	- [[ImageNet]]
	- [[Position Encoding]] , a crucial component in existing Vision Transformers, can be safely removed in our model
	- potential advantage for adaption
	- built-in local context structure introduced by convolutions, CvT no longer requires a position [embedding](Embedding.md)








