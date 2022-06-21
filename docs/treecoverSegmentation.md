---
title: Tree Cover Segmentation
tags: application
---

# Tree Cover Segmentation
- treecover segmentation [[PointNet++]]
	- Data collected from above
	- Normalization : height, xy
	- Rotation
	- Jiggling ??
	- Labeling
		- ![[../assets/Pasted image 20220318094643.png]] Segmentation algorithm. Canopy hide model
		- Weighted loss + [[Focal Loss]]
## 2d Methods
- [[Watershed]] + [[Unet]]
- ![[../assets/Pasted image 20220318100323.png]]
- ![[../assets/Pasted image 20220318100634.png]]
	- $\Theta$ is just clippingpng]]
	- The sqrt makes it a little smoother
## Ref
- Max Freudenberg - Gottingen Uni Germany
- Adrian Stroker - Gottingen Uni Germany

































