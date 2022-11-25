---
title: Vision Explainibility

tags: mastersthesis explainability flow
date modified: Friday, November 18th 2022, 2:05:31 pm
date created: Friday, November 18th 2022, 12:31:29 pm
---

# Vision Explainibility
```toc
```

## Flow
- [DeconvNet](DeconvNet.md)
- [Deep_Inside_Convolutional_Networks](Deep_Inside_Convolutional_Networks.md)
- [Guided_BackProp](Guided_BackProp.md)
- [Salience_Map](Salience_Map.md)
	- Not class discriminative
	- Noise
	- Not appealing
- [Guided_BackProp](Guided_BackProp.md)
	- Building up on [Deep_Inside_Convolutional_Networks](Deep_Inside_Convolutional_Networks.md)
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
	- ![](images/Pasted%20image%2020221118132213.png)
	
```mermaid

graph TD;
E1[Guided BackProp] --> A
E2[DeconvNet] --> A
E3[Deep Inside Convolutional Networks] --> A
A[[Salience Map]] --> B[[CAM]] --> C[[GradCAM]] --> E[Guided GradCAM]
A --> F[Occlusion Map] --> E
E --> D[GradCAM++]

E4[Network In Network] --> B
class A internal-link
class B internal-link
class C internal-link
class D internal-link
class E internal-link
class F internal-link
class E1 internal-link
class E2 internal-link
class E3 internal-link
class E4 internal-link
```

