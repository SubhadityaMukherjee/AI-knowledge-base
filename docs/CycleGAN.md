---
title: CycleGAN

tags: architecture generative
date modified: Monday, December 12th 2022, 12:47:17 am
date created: Sunday, December 11th 2022, 12:58:09 pm
---

# CycleGAN
```toc
```
- Unpaired image2image
- 2 Mapping functions G, F : generator and $D_{X}, D_{Y}$ as generators
- [[Adversarial Loss]]
- $\mathcal{L}_{cyc}$ [[Cycle Consistency Loss]]
- Full objective
	- Adversarial Loss + [[Cycle Consistency Loss]]
	- $\lambda$ is a hyperparam. Generally set to 10
	- $$\mathcal{L}_{GAN}(G, F, D_{X}, D_{Y}) = \mathcal{L}_{GAN}(G, D_{Y}, X, Y) + \mathcal{L}_{GAN}(F, D_{X}, X, Y) + \lambda \mathcal{L}_{cyc}(G,F)$$
- To Solve
- $$G^{*},F^{*} =\underset{G,F}{argmin} \underset{D_{X}, D_{Y}}{max} \mathcal{L}_{GAN}(G, F, D_{X}, D_{Y})$$
- two stride-2 convolutions, several residual blocks, and two fractionally strided convolutions with stride $\frac{1}{2}$
- [[Instance Normalization]]

## Architecture

## Generator
- ![[Pasted image 20221211132006.png]]

### Encoder
- The encoder extracts features from the input image by using Convolutions and compressed the representation of image but increase the number of channels
- The encoder consists of 3 convolution that reduces the representation by 1/4 th of actual image size

### Transforming Block
- The transformer contains 6 or 9 residual blocks based on the size of input.
- The output of transformer is then passed into the decoder which uses 2 -deconvolution block of fraction strides to increase the size of representation to original size.

## Discriminator
- [[PatchGAN]]

## Applications
- Style Transfer
	- Unlike other works on neural style transfer, CycleGAN learns to mimic the style of an entire collection of artworks, rather than transferring the style of a single selected piece of art
- Object Transformation
	- CycleGAN can transform object from one ImageNet class to another such as: Zebra to Horses and vice-versa, Apples to Oranges and vice versa etc
- Season Transfer
	- CycleGAN can also transfer images from Winter Season to Summer season and vice-versa. For this the model is trained on 854 winter photos and 1273 summer photos of Yosemite from Flickr.
- Photo Generation from Painting
	- can also be used to transform photo from paintings and vice-versa
	- [[Identity Loss]]

## Limits
- applied to perform geometrical transformation, CycleGAN does not perform very well. This is because of the generator architecture which is trained to perform appearance changes in the image.

## Reduce Model Oscillation
- To prevent the model from changing drastically from iteration to iteration, the discriminators were fed a history of generated images, rather than just the ones produced by the latest versions of the generator.
- To do this we keep storing the 50 most recently generated images. Based on this technique we reduce the model Oscillation as well as model overfitting.

## Backlinks

> - [](journals/2022-12-11.md)
>   - **12:57** Have to write an article about [[CycleGAN]]

_Backlinks last generated 2022-12-12 23:44:06_
