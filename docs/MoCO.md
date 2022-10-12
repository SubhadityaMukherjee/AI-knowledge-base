---
tags: temp
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: MoCO

tags: architecture

---

# MoCO
- [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722)
- unsupervised visual representation learning
- contrastive learning as dictionary look-up, MoCo builds a dynamic dictionary with a queue and a moving-averaged encoder
- large and consistent dictionary on-the-fly
- [[ImageNet]]
- transfer well to downstream tasks.
- [[PASCAL VOC]]
- [[COCO]]
- visual representation encoder by matching an encoded query
- to a dictionary of encoded keys using a [[Contrastive Loss|contrastive loss]]
- dictionary is built as a queue, with the current mini-batch enqueued
- oldest mini-batch dequeued
- slowly progressing encoder
- momentum update with the query encoder
- ![[assets/moco1.jpg]]
- ![[assets/moco2.jpg]]

## Backlinks
> - [Self Supervised Vision Transformers](Self Supervised Vision Transformers.md)
>   - [[MoCO]] v3, a framework which offers an incremental improvement of [[MoCO]]
>   - [[MoCO]] v3, a framework which offers an incremental improvement of [[MoCO]]

_Backlinks last generated 2022-10-04 13:01:19_
