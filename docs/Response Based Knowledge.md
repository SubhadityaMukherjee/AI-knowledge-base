---
title: Response Based Knowledge

tags: knowledgedistillation 
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:43:35 am
---

# Response Based Knowledge
- neural response of the last output layer of the teacher model. The main idea is to directly mimic the final prediction of the teacher model.
- Given a vector of [[Logits|logits]] z as the outputs of the last fully connected layer of a deep model, the [[distillation loss]] for response-based knowledge can be formulated as
- response in object detection task may contain the [[Logits|logits]] together with the offset of a bounding box (Chen et al., 2017). In semantic landmark localization tasks, e.g., human pose estimation, the response of the teacher model may include a heatmap for each landmark (Zhang et al., 2019a)

## Backlinks
> - [Knowledge Distillation Survey 2021](Knowledge Distillation Survey 2021.md)
>   - [[Response Based Knowledge]]

_Backlinks last generated 2022-10-04 13:01:19_
