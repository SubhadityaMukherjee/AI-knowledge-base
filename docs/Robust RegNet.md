---
tags: temp
date modified: Thursday, August 11th 2022, 12:32:46 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: Robust RegNet

tags: architecture

---

# Robust [[RegNet]]
- [Vision Models are More Robust and Fair When Pretrained on Uncurated Images Without Supervision](https://arxiv.org/abs/2202.08360)
- [[Unsupervised Learning]]
- Discriminative [[Self Supervised]] learning allows training models on any random group of internet images, and possibly recover salient information that helps differentiate between the images
- [[ImageNet]]
- object-centric [[Features|features]] that perform on par with supervised [[Features|features]] on most object-centric downstream tasks
- learn any salient and more representative information present in diverse unbounded set of images from across the globe
- without any data pre-processing or prior assumptions about what we want the model to learn
- [[RegNet]]
- scaled to a dense 10 billion parameters
- pre-trained using the [[SwaV]] self-supervised method on a large collection of 1 billion randomly selected public images from Instagram with a diversity of gender, ethnicity, cultures, and locations
- captures well semantic information
- captures information about artistic style and learns salient information such as geo-locations and multilingual word embeddings based on visual content only.
- large-scale self-supervised pre-training yields more robust, fair, less harmful, and less biased results than supervised models or models trained on object centric datasets such as [[ImageNet]]

