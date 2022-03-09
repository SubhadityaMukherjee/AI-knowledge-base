# Convnd
- Connect a neighbor only to spatial neighborhood -> spatial order
	- Some rotation and illumination invariance
- Slide over -> Same weights independant of location -> less weights
- Subsample after conv
- multiple 2d feature maps
- Similar to Gabor filters after learning
- Some might collapse to 0
- $out(x,y) = \Sigma_i \Sigma_j input(x+i, y+j) kernel(i,j)$
- $Z^j = \Sigma_{i=0}^{l-1}W^{ji} \ast X^i + b^{ij}$
- $Y^j = g(Z^j)$
- Output shape : $\frac{()_i-f+2p}{s}$
	- If $p = \frac{f-1}{2}$ and $s=1$ then dimensions maintained

## Padded Conv
- $(N_i, N_o, C, F)$
- Filters transform from C -> F channels
- Mirror, Reflect

## Strided
- Normally S = 1
- S>1 -> Downsampling 
- Dilated
- Spaces in the filter kernel
- D = 1 : normal conv aka D-1 spaces
- Effective Filter size : $\hat F = F + (F-1)(D-1)$

## Depthwise Separable
- Only transforms the input once and saves computation -> elongate it to more channels
- From C -> F channels : Use F instances of a 1x1xC filter
- ![[Pasted image 20220306122226.png]]

## Causal 1D Conv
- Only past info used for prediction
- Conv works in both directions and can leak future information into predictions

## Causal Dilated Conv
- Receptive field is how much of the input sequence is needed for one prediction
## [[Conv]]