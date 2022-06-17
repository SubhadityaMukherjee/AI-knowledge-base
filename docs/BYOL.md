
---

title: BYOL

tags: architecture 

---

# BYOL
- [Bootstrap Your Own Latent: a New Approach to Self-supervised Learning](https://arxiv.org/abs/2006.07733)
	- [[Self supervised]] image representation learning
	- predicting previous versions of its outputs, without using negative pairs
	- two neural networks, referred to as online and target networks
	- that interact and learn from each other
	- From an augmented view of an image, they train the [[Online Learning]] network to predict the target network representation of the same image under a different augmented view
	- update the target network with a slow-moving average of the online network
	- [[ImageNet]]
	- [[Res Net]]
	- dependent on existing sets of [[Augmentation]] that are specific to vision applications
	- [[BYOL Loss]]
	  id:: 62a8aa38-6fee-480e-9fc7-5511c0ae6836






