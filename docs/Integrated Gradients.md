---
title: Integrated Gradients
tags: explainability mastersthesis 
date modified: Tuesday, December 6th 2022, 12:46:40 pm
date created: Tuesday, December 6th 2022, 12:46:39 pm
---

# Integrated Gradients
- @sundararajanAxiomaticAttributionDeep2017
```toc
```
## Terms
- [[Gradient Sensitivity]]
- [[Implementation Invariance]]

## Calculation

- a function F representing our model
- input $x \in \mathbb{R}^{n}$ because this is a general definition of IG and not CNN specific),
- baseline $x' \in \mathbb{R}^{n}$
- We assume a straight line path between x and x' and compute gradients along that path
- The integrated gradient along $i^{th}$ dimension is defined as:
- $$IntegratedGrads_i​(x)::=(x_i​-x_i'​)\times \int_{\alpha=0}^{1}\frac{\partial F(x' + \alpha \times (x-x'))}{\partial x_{i}}d \alpha$$
- The original definition of Integrated Gradients is incalculable (because of the integral).
- Therefore, the implementation of the method uses approximated value by replacing the integral with the summation:
- $$IntegratedGrads_i​^{approx}(x)::=(x_i​-x_i'​)\times \Sigma_{k=1}^{m}\frac{\partial F(x' + \frac{k}{m} \times (x-x'))}{\partial x_{i}} \times \frac{1}{m}$$
- In the approximated calculation (Eq. 2), m defines a number of interpolation steps.

## Explanation (chatgpt)
- In IntegratedGrads, the goal is to understand the contribution of each pixel in the input image towards the model's prediction. Specifically, for a given pixel $i$, IntegratedGrads computes the partial derivative of the model output with respect to that pixel and integrates it along a path from a baseline image to the input image, weighting each step of the path by the partial derivative.
- The equation you provided is an approximation of IntegratedGrads, which involves dividing the path into $m$ equally spaced steps and approximating the integral using a Riemann sum. Let's break down the equation using an example of an image of a bird:
- $IntegratedGrads_i^{approx}(x)$ represents the attribution of pixel $i$ towards the model's prediction, using the IntegratedGrads approximation.
- $(x_i-x_i')$ is the difference between the input image pixel $i$ and the baseline pixel $i'$.
- $\Sigma_{k=1}^{m}$ is a sum over the $m$ steps of the path from the baseline image to the input image.
- $\frac{\partial F(x' + \frac{k}{m} \times (x-x'))}{\partial x_i}$ is the partial derivative of the model output $F$ with respect to pixel $i$ at the $k$-th step of the path, where $x' + \frac{k}{m} \times (x-x')$ is the image at that step.
- $\frac{1}{m}$ is a weighting factor that ensures that each step of the path is given equal importance in the approximation.
- For example, let's say we have an image of a bird and we want to understand the contribution of the pixel at position $(10, 20)$ towards the model's prediction that the image is a bird. We set the baseline pixel value to be zero and divide the path into 10 steps. We compute the partial derivative of the model output with respect to pixel $(10, 20)$ at each step of the path and weight each step by $\frac{1}{10}$ to obtain the approximation of IntegratedGrads for pixel $(10, 20)$. The resulting attribution value will give us an indication of how important that pixel is in the model's prediction.

## Baselines

- replacing the constant color baseline with an alternative
- [[Gaussian Baseline]]
- [[Blur Baseline]]
- [[Visualizing the Impact of Feature Attribution Baselines]]


## Backlinks

> - [Conductance](Conductance.md)
>   - This paper introduces the concept of conductance as a way to understand the importance of hidden units in deep networks. Conductance is defined as the flow of [[Integrated Gradients]]' attribution via a hidden unit, and is used to understand the importance of a hidden unit to the prediction for a specific input or over a set of inputs. The effectiveness of conductance is evaluated in multiple ways, including theoretical properties, ablation studies, and a feature selection task using the Inception network over ImageNet data and a sentiment analysis network over reviews. The properties of conductance include completeness, linearity and insensitivity to variations in inputs or hidden unit values. The paper also discusses the issue of saturation in neural networks, where the gradient of the output with respect to the input can be near-zero, and how conductance addresses this issue. The authors also compare conductance with other methods of understanding hidden unit importance and find it to be more intuitive and accurate.
>   - Informally, the conductance of a hidden unit of a deep network is the flow of [[Integrated Gradients]]' attribution via this hidden unit
>   - The key idea behind conductance is to decompose the computation of [[Integrated Gradients]] via the chain rule
>   - [[Integrated Gradients]] produces attributions for base features
>   - [[Integrated Gradients]] is path integral of gradient along straightline path from baseline $x'$ to input $x$. The function F varies from a near zero value for the informationless baseline to its final value. The gradients of F with respect to the image pixels explain each step of the variation in the value of F
>   - As an artificial example, suppose the network first transforms the input x linearly to y = 2x, and then transforms it to z = max(y, 1). Suppose the input is x = 1 (where z is saturated at value 1), with 0 being the baseline. Then for the hidden unit of y, gradient of z w.r.t. y is 0. Gradient\*activation would be 0 for y, which does not reflect the intuitive importance of y. Like in [[Integrated Gradients]], in computing conductance, we consider all extrapolated inputs for x between 0 and 1, and look at the gradients of output w.r.t. y at these points. This takes the non-saturated region into account, and ends up attributing 1 to y, as desired.
>    
> - [Vision Explainibility](Vision Explainibility.md)
>   - [[Integrated Gradients]]
>    
> - [Smooth-Grad](Smooth-Grad.md)
>   - reduces visual noise and, hence, improves visual explanations about how a DNN is making a classification decision. Comparing their work to several gradient-based sensitivity map methods such as LRP, [[DeepLift]], and [[Integrated Gradients]] (IG) [96], which estimate the global importance of each pixel and create saliency maps, showed that Smooth-Grad focuses on local sensitivity and calculates averaging maps with a smoothing effect made from several small perturbations of an input image. The effect is enhanced by further training with these noisy images and finally having an impact on the quality of sensitivity maps by sharpening them.

_Backlinks last generated 2023-01-28 14:37:47_
