---
title: Tree Cover Segmentation
tags: application
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Tree Cover Segmentation
- treecover segmentation [[PointNet++]]
	- Data collected from above
	- Normalization : height, xy
	- Rotation
	- Jiggling ??
	- Labeling
		- ![[assets/Pasted image 20220318094643.png|im]] Segmentation algorithm. Canopy hide model
		- Weighted [[loss]] + [[Focal Loss]]

## 2d Methods
- [[Watershed]] + [[Unet]]
- ![[assets/Pasted image 20220318100323.png|im]]
- ![[assets/Pasted image 20220318100634.png|im]]
	- $\Theta$ is just clippingpng]]
	- The sqrt makes it a little smoother

## Ref
- Max Freudenberg - Gottingen Uni Germany
- Adrian Stroker - Gottingen Uni Germany

