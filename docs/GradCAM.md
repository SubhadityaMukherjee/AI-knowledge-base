---
title: GradCAM

tags: architecture 
---

# GradCAM
- [Grad-CAM: Visual Explanations from Deep Networks Via Gradient-based Localization](https://arxiv.org/abs/1610.02391)
- producing ‘visual explanations’ for decisions from a large class of CNN-based models, making them more transparent and explainable
- Gradient-weighted Class Activation Mapping
- uses the gradients of any target concept
- flowing into the final convolutional layer to produce a coarse localization map highlighting the important regions in the image for predicting the concept
- lend insights into failure modes of these models (showing that seemingly unreasonable predictions have reasonable explanations)
- are robust to adversarial perturbations
- are more faithful to the underlying model
- help achieve model generalization by identifying dataset bias
- identify important neurons through GradCAM and combine it with neuron names to provide textual explanations for model decisions


## Backlinks

> - [](journals/2022-06-27.md)
>   - [[GradCAM]]

_Backlinks last generated 2022-06-27 22:06:24_
