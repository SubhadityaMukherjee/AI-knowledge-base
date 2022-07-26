
---

title: Neural Radiance Field

tags: architecture 

---

# Neural Radiance Field
- [NeRF: Representing Scenes As Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934)
	- synthesizing novel views of complex scenes
	- optimizing an underlying continuous volumetric scene function using a sparse set of input views
	- single continuous 5D coordinate (spatial location (x,y,z) and viewing direction (θ,ϕ))
	- output is the volume density and view-dependent emitted radiance at that spatial location
	- querying 5D coordinates along camera rays
	- volume rendering techniques to project the output colors and densities into an image
	- volume rendering is naturally differentiable
	- set of images with known camera poses
	- They describe how to effectively optimize neural radiance fields to render photorealistic novel views of scenes


















































































## Backlinks

> - [BlockNeRF](BlockNeRF.md)
>   - variant of [[Neural Radiance Field]]
>    
> - [Instant NeRF](Instant NeRF.md)
>   - [[Neural Radiance Field]]

_Backlinks last generated 2022-07-26 20:33:15_
