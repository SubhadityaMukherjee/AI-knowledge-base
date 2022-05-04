---
title: Tree Cover Segmentation
---

# Tree Cover Segmentation
- treecover segmentation [[PointNet++]]
	- Data collected from above
	- Normalization : height, xy
	- Rotation
	- Jiggling ?? 
	- Labeling
		- ![[Pasted image 20220318094643.png]] Segmentation algorithm. Canopy hide model
		- Weighted loss + [[Focal Loss]]

## 2d Methods
- [[Watershed]] + [[Unet]]
- ![[Pasted image 20220318100323.png]]
- ![[Pasted image 20220318100634.png]]
	- $\Theta$ is just clipping
	- The sqrt makes it a little smoother

## Ref
- Max Freudenberg - Gottingen Uni Germany
- Adrian Stroker - Gottingen Uni Germany






