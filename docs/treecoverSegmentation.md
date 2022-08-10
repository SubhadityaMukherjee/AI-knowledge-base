---
title: Tree Cover Segmentation
tags: application
date modified: Thursday, August 11th 2022, 12:32:42 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Tree Cover Segmentation
- treecover segmentation [PointNet++](PointNet++.md)
	- Data collected from above
	- Normalization : height, xy
	- Rotation
	- Jiggling ??
	- Labeling
		- ![im](assets/Pasted%20image%2020220318094643.png) Segmentation algorithm. Canopy hide model
		- Weighted [loss](loss.md) + [Focal Loss](Focal%20Loss.md)

## 2d Methods
- [Watershed](Watershed) + [Unet](Unet.md)
- ![im](assets/Pasted%20image%2020220318100323.png)
- ![im](assets/Pasted%20image%2020220318100634.png)
	- $\Theta$ is just clippingpng]]
	- The sqrt makes it a little smoother

## Ref
- Max Freudenberg - Gottingen Uni Germany
- Adrian Stroker - Gottingen Uni Germany

