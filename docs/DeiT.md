---
tags: temp
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: DeiT

tags: architecture

---

# DeiT
- [paper](https://arxiv.org/abs/2012.12877)
- [blog](https://ai.facebook.com/blog/data-efficient-image-transformers-a-promising-new-technique-for-image-classification/)
- [[Conv]] free [[Transformer]], [[Vision Transformer]]
- does not require very large amount of data
  id:: 62a8a66a-941e-4a6d-918a-bb49cd496b15
- [[Knowledge Distillation]]
- teacher-student strategy specific to transformers
- [[Distillation Token]]
- ConvNet as teacher through [[Attention]]
  id:: 62a8a6b2-abf4-4869-934e-c75d05884304
- [[ImageNet]]
- #+BEGIN_CAUTION
  Heh. Didnt they say no convs?
  #+END_CAUTION

## Backlinks
> - [BEiT](BEiT.md)
>   - outperforming from-scratch [[DeiT]]

_Backlinks last generated 2022-10-04 13:01:19_