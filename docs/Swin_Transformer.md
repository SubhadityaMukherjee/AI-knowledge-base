---
tags: temp
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: Swin Transformer

tags: architecture

---

# Swin [Transformer](Transformer.md)
- [Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows](https://arxiv.org/abs/2103.14030)
	- [Vision_Transformer](Vision_Transformer.md)
	- general-purpose backbone for computer vision
	- hierarchical feature representation
	- linear computational complexity with respect to input image size
	- shifted window based [Self_Attention](Self_Attention.md)
	- address the challenges in adapting [Transformer](Transformer.md) from language to vision
	- limiting self-[attention](Attention.md) computation to non-overlapping local windows while also allowing for cross-window connection
	- flexibility to model at various scales
	- linear computational complexity with respect to image size
	- [ImageNet](ImageNet.md)
	- [COCO](COCO.md)
	- [ADE20K](ADE20K.md)
	- The hierarchical design and the shifted window approach also prove beneficial for all [Perception](Perception.md) [Architectures](Architectures).
	- Ratio of 1:1:3:1

