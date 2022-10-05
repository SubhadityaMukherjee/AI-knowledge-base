---
title: GradCAM

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
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

> - [Embedding Human Knowledge into Deep Neural Network via Attention Map](Embedding Human Knowledge into Deep Neural Network via Attention Map.md)
>   - Typical visual explanation approaches in- clude class activation mapping (CAM) and [[GradCAM]]
>    
> - [Generalizing Adversarial Explanations with Grad-CAM](Generalizing Adversarial Explanations with Grad-CAM.md)
>   - The drawback of [[GradCAM]] is that it cannot be used to generalize CNN behaviour.

_Backlinks last generated 2022-10-05 15:25:18_
