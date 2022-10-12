---
title: MVGrasp

tags: robotics architecture 
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# MVGrasp
- H. Kasaei, et al. "MVGrasp: Real-Time Multi-View 3D Object Grasping in Highly Cluttered Environments." arXiv preprint arXiv:2103.10997 (2021).
- Render multiple views of objects and use a next best view view selection algorithm Generate pixel-wise grasp configuration for the given object view.  
- The [[Gripper|gripper]] approaches the target object in an arbitrary direction.  
- Use a shallow network, and an eye-to-hand camera configuration.
- ![[assets/Pasted image 20220928214219.png]]
- Mixed autoencoder (CAE + DAE)  
- optimizer: RMSprop, learning_rate = 0.001  
- metrics: Intersection over Union (IoU) and reconstruction error loss: mean squared error
- ![[assets/Pasted image 20220928214247.png]]
- Which view is suitable?
	- Depends on the pose of the target object and other objects  
	- Most objects are graspable from either top or side -> orthographic setup
	- View [[Entropy|entropy]] is used as the metric for selecting the best view

## Backlinks
> - [[Grasp Point Detection]]
>   - [[GGCNN]], [[GRConvNet]], [[.md|MVGrasp]], [[Unet Grasping]], [[Learning to Detect Grasp Affordance]], [[Volumetric Grasping Network]] , [[Affordance Detection Task Specific]]

_Backlinks last generated 2022-10-03 15:37:32_
