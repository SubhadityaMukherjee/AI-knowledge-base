- #architecture
- [paper](https://arxiv.org/abs/2010.11929)
  id:: 62a8a619-06c3-464d-bcbd-4fdf7534d1de
- ![](../assets/vit.png)
  id:: 62a8a207-b2e6-41dc-ab5c-a47f2a492223
- Transformer applied directly to sequences/patches of images
- Lower computational resources
- [[ImageNet]] , [[CIFAR]], [[VTAB]]
- [Do Vision Transformers See Like Convolutional Neural Networks?](https://arxiv.org/abs/2108.08810)
	- analyzes the internal representation structure of ViTs and [[Conv]] on image classification benchmarks
	- striking differences in the features and internal structures between the two architectures
	- ViT having more uniform representations across all layers
	- early aggregation of global information
	- spatial localization
	- discovering ViTs successfully preserve input spatial information with CLS tokens
	- finding larger ViT models develop significantly stronger intermediate representations through larger pretraining datasets
	- [[MLP-Mixer]]

