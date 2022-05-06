---
title: Convnd
tag: architecture
---

# Convnd
- $$A\ast B$$
- Connect a neighbor only to spatial neighborhood -> spatial order
	- Some rotation and illumination invariance
- Slide over -> Same weights independant of location -> less weights
- Subsample after conv
- multiple 2d feature maps
- Similar to Gabor filters after learning
- Some might collapse to 0
- $$out(x,y) = \Sigma_i \Sigma_j input(x+i, y+j) kernel(i,j)$$
- $$Z^j = \Sigma_{i=0}^{l-1}W^{ji} \ast X^i + b^{ij}$$
- $$Y^j = g(Z^j)$$
- Output shape : $$\frac{()_i-f+2p}{s}$$
	- If $$p = \frac{f-1}{2}$$ and $$s=1$$ then dimensions maintained
- One operation repeated over and over starting with raw

- [[Padded Conv]]

- [[Strided]]

- [[Depthwise Separable]]

- [[Causal 1D Conv]]

- [[Causal Dilated Conv]]














