---
toc: true
title: KeepAugment
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# KeepAugment
- KeepAugment identifies the salient area in an image and assures the image generated by the augmentation strategies, for example, [Cutout], [RandAugment] [14], [CutMix] [82] or [AutoAugment](Cutout], [RandAugment] [14], [CutMix] [82] or [AutoAugment.md) [13], contains salient region in it.
- standard augmentation may introduce distribution shifts
- increase fidelity of the augmented data
- use saliency maps to identify the regions of interest, then make sure those regins are not affected by the augmentation
- Given image $x$ and label logit value $l_{y}$ , $g_{i,j}(x,y)$ to be the vanilla gradient $|\nabla_{x}l_{y}(s)|$ 
- For RGB, channel wise maximum to get single saliency value for each pixel $(i,j)$

## Selective Cut
- Randomly sample regions $S$ to be cut until importance score $\mathcal{I}(S, x, y)$ is smaller than threshold $\tau$ 
$$
\tilde x= (1-M(S)) \odot x$$
- where $M(S) = |M_{ij}(S)|_{ij}$ is the binary mask for $S$, $M_{ij} = \mathbb{I}((i,j) \in S)$

## Selective Paste
- image level augmented data $x' = \mathcal{A}(x)$ , uniformly sample region $S$ that satisfies $\mathcal{I}(S,x,y) > \tau$ for a threshold $\tau$ 
- paste the region $S$ of the original image  $x$ to $x'$ 
	- $$\tilde x = M(S) \odot x + (1-M(S)) \odot x'$$
	- $M_{ij}(S) = \mathbb{I}((i,j) \in S)$ is the binary mask of the region $S$
- we choose our threshold $\tau$ in an adaptive way.
- given an image and consider an region size h × w of interest, we first calculate the importance scores of all possible candidate regions, following Eq. 1; then we set our threshold to be the $\tau - quantile$ value of all the importance scores $\mathcal{I}(S,x,y)$ of all candidate regions. For selective-cut, we uniformly keep sampling a mask region S until its corresponding score $\mathcal{I}(S,x,y)$ is smaller than the threshold. For selective-paste, we uniformly sample a region S with importance score is greater than the threshold

## Efficient Implementation of KeepAugment

### Low Resolution Based Approximation
- we proceed as follows: a) for a given image x, we first generate a lowresolution copy and then calculate its saliency map; b) we map the low-resolution saliency maps to their corresponding original resolution
- This allows us to speed up the saliency maps calculation significantly, e.g., on ImageNet, we achieve roughly 3× computation cost reduction by reducing the resolution from 224 to 112.

### Early Classification Head Based Approximation
- In practice, we add an additional average pooling layer and a linear head after the first block of our networks evaluated
- We achieve about 3× computation cost reduction in computing saliency maps

## Region-Level Augmentation
- including Cutout [8] and random erasing [45], work by randomly masking out or modifying rectangular regions of the input images
- This procedure could be conveniently formulated as applying randomly generated binary masks to the original inputs
- Precisely, consider an input image x of size H × W, and a rectangular region S of the image domain. Let M(S) = [Mij (S)]ij be the binary mask of S with Mij (S) = I((i, j) ∈ S)
- Then the augmented data can be generated by modifying the image on region S, yielding images of form x′ = (1 − M(S)) ⊙ x + M(S) ⊙ δ, where ⊙ is element-wise multiplication, and δ can be either zeros (for Cutout) or random numbers (for random erasing)

## Image-Level Augmentation
- Exploiting the invariance properties of natural images, image-level augmentation methods apply label-invariant transformations on the whole image, such as solarization, sharpness, posterization, and color normalization
- often manually designed and heuristically chosen
- Recently, AutoAugment [4] applies reinforcement learning to automatically search optimal compositions of transformations
- Several subsequent works, including RandAugment [5], Fast AutoAugment [18], alleviate the heavy computational burden of searching on the space of transformation policies by designing more compact search spaces

## Data Augmentation and Its Trade-offs
- Although data augmentation increases the effective size of data, it may inevitably cause loss of information and introduce noise and ambiguity if the augmentation is not controlled properly
- To study this phenomenon empirically, we plot the train and testing accuracy on CIFAR-10 [16] when we apply Cutout with increasingly large cutout length in Figure 2(a), and RandAugment with increasing distortion magnitude 
- As typically expected, the generalization (the gap between the training and testing accuracy on clean data) improves as the magnitude of the transform increases in both cases
- However, when the magnitudes of the transform are too large (≥ 16 for Cutout and ≥ 12 for RandAugment ), the training accuracy (blue line), and hence the testing accuracy (red line), starts to degenerate, indicating that augmented data no longer faithfully represent the clean training data in this case, such that the training loss on augmented data no longer forms a good surrogate of the training loss on the clean data.

## Images
- ![](../images/Pasted%20image%2020230508121420.png)
- ![](../images/Pasted%20image%2020230508121431.png)
- ![](../images/Pasted%20image%2020230508121452.png)
- ![](../images/Pasted%20image%2020230508121458.png)



