---
title: GradCAM

tags: architecture 
date modified: Friday, November 18th 2022, 1:24:54 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GradCAM
- [Grad-CAM: Visual Explanations from Deep Networks Via Gradient-based Localization](https://arxiv.org/abs/1610.02391)
- Modified [[CAM]]
- Importance of feature map k for target class c
	- A is input
	- $Y_{c}=\text{score of class c}$ : value of output before softmax
	- grad of $Y_{c}$ wrt A and take avg
	- $$\alpha_{k}^{c}= average(\partial \frac{Y_{c}}{\partial A^{k}_{ij}})$$
	- If avg is high : important
	- 0 : not
	- neg : background/ others
- Weighted combination -> relu
	- $$L^{c}_{GRADCAM}=Resize(ReLU(\Sigma_{k}(\alpha^{c}_{k}A^{k})))$$
	- This is a coarse heatmap because the image is resized
	- ReLU used because we only care about positive values (actualy image pixel)
- To identify [[Counterfactual Images]], flip the signs
	- $$\alpha_{k}^{c}=average(- \partial \frac{Y_{c}}{\partial A^{k}_{ij}})$$
	- ![](images/Pasted%20image%2020221118132132.png)
- Followed by [[Guided GradCAM]]

## Predicting Failure Modes
- ![](images/Pasted%20image%2020221118132330.png)

## Adversarial Noise
- robust to
- ![](images/Pasted%20image%2020221118132412.png)

## Removing Biasness
- ![](images/Pasted%20image%2020221118132453.png)

## Other Stuff
- producing ‘visual explanations’ for decisions from a large class of CNN-based models, making them more transparent and explainable
- Gradient-weighted Class Activation Mapping
- uses the gradients of any target concept
- flowing into the final convolutional layer to produce a coarse localization map highlighting the important regions in the image for predicting the concept
- lend insights into failure modes of these models (showing that seemingly unreasonable predictions have reasonable explanations)
- are robust to adversarial perturbations
- are more faithful to the underlying model
- help achieve model generalization by identifying dataset bias
- identify important neurons through GradCAM and combine it with neuron names to provide textual explanations for model decisions

