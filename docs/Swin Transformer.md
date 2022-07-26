
---

title: Swin Transformer

tags: architecture

---

# Swin [[Transformer]]
- [Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows](https://arxiv.org/abs/2103.14030)
	- [[Vision Transformer]]
	- general-purpose backbone for computer vision
	- hierarchical feature representation
	- linear computational complexity with respect to input image size
	- shifted window based [[Self Attention]]
	- address the challenges in adapting [[Transformer]] from language to vision
	- limiting self-[[Attention|attention]] computation to non-overlapping local windows while also allowing for cross-window connection
	- flexibility to model at various scales
	- linear computational complexity with respect to image size
	- [[ImageNet]]
	- [[COCO]]
	- [[ADE20K]]
	- The hierarchical design and the shifted window approach also prove beneficial for all [[Perception]] [[Architectures]].
	- Ratio of 1:1:3:1
















## Backlinks

> - [ConvNeXt](ConvNeXt.md)
>   - hierarchical Transformers (e.g., [[Swin Transformer]] ) that reintroduced several [[Conv]] priors, making Transformers practically viable as a generic vision backbone

_Backlinks last generated 2022-07-26 20:33:15_
