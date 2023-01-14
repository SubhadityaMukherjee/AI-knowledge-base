---
title: Vision Explainibility

tags: mastersthesis explainability flow
date modified: Saturday, January 14th 2023, 4:36:15 pm
date created: Friday, November 18th 2022, 12:31:29 pm
---

# Vision Explainibility

## Links Useful
- [Captum Algos Comparison](https://captum.ai/docs/algorithms_comparison_matrix)

## Flow
- [DeconvNet](DeconvNet.md) (2013)
- [Deep_Inside_Convolutional_Networks](Deep_Inside_Convolutional_Networks.md) (2014)
- [Guided_BackProp](Guided_BackProp.md) (2015) Aka All Conv net
	- Building up on [Deep_Inside_Convolutional_Networks](Deep_Inside_Convolutional_Networks.md) and [[DeconvNet]]
- [Salience_Map](Salience_Map.md)
	- Not class discriminative
	- Noise
	- Not appealing
- [CAM](CAM.md)
	- less noisy
	- not class discriminative
	- Worked only a restricted set of CNN templates
- [GradCAM](GradCAM.md)
	- class discriminative
	- not high res
	- Works for any arbitrary CNN
- [Occlusion Map](Occlusion%20Map)
	- Same as the next but not very fast
- [Guided_GradCAM](Guided_GradCAM.md)
- [[DeepLIFT]]
- [[Noise Tunnel]]
- [[Smooth-Grad]]
- [[SmoothGrad Square]]
- [[VarGrad]]
- [[Integrated Gradients]]
- [[Proxy Attention]]
- [[Conductance]]

## Disadvantages
- [[The Unreliability of Saliency Methods]]
- [[Interpretation of Neural networks is fragile]]
- Fine grained data
	
```mermaid

graph TD;
E2[DeconvNet] --> E1
E3[Deep_Inside_Convolutional_Networks] --> E1
E1[Guided_BackProp]

B1[CAM] --> B2[GradCAM] --> B3[GradCAM++]
B2 --> B4[Guided_GradCAM]

E4[Network In Network] --> B1


E1 --> B4

E2 --> A[Salience_Map]
E3 --> A
E1 --> A

C0[Integrated Gradients] --> C1
E1 --> C1
C1[Smooth-Grad] --> C4
C2[SmoothGrad Square] --> C4
C3[VarGrad] --> C4
C0 --> C5[Conductance]
C4[Noise Tunnel] --> P
C0 --> P
C4 --> P
A --> P
B2 --> P

subgraph proposed
P([Proxy Attention])
end

U1[The Unreliability of Saliency Methods] --Changes break saliency--> A
U2[Interpretation of Neural networks is fragile] --Adversarial Attacks--> A
class A internal-link
class B internal-link
class B1 internal-link
class B2 internal-link
class B3 internal-link
class B4 internal-link
class C internal-link
class C0 internal-link
class C1 internal-link
class C2 internal-link
class C3 internal-link
class C4 internal-link
class C5 internal-link
class D internal-link
class E internal-link
class F internal-link
class E1 internal-link
class E2 internal-link
class E3 internal-link
class E4 internal-link
class U1 internal-link
class U2 internal-link
class P internal-link
```

## Backlinks
> - [](journals/2022-12-06.md)
>   - **12:01** [[Vision_Explainibility]]
>
> - [](journals/2022-12-09.md)
>   - **11:05** Bunch of things today. First I have a thesis presentation [[Vision_Explainibility]], then an article on [[Masked Language Modeling]] and then Cogmod

_Backlinks last generated 2022-12-12 23:44:06_
