---
title: Pooling
tag: architecture
---

# Pooling
- Summarize low level [[Features|features]]
- Reduce input dims
- Max/Avg
- Too much pooling reduces performance
	- Multiple convs first 
- Max pool + dilated/[[Strided]] convs control effective [[Receptive field|receptive field]] size


































































































## Backlinks

> - [ConvNeXt](ConvNeXt.md)
>   - The second is the stem cell configuration, which in the original ResNet consisted of 7×7 convolutions with stride 2 followed by a max-[[Pooling]] layer. This was substituted by a more [[Transformer]]-like “patchify” layer which utilizes 4×4 non-overlapping convolutions with stride 4
>    
> - [Discrete Cosine Transform](Discrete Cosine Transform.md)
>   - In my opinion, this can be explained by looking at the internals of a convolutional layer. It works as follows. You specify a number of filters which, during training, learn to recognize unique aspects of the image-like data. They can then be used to classify new samples - quite accurately, as we have seen with raw [[MNIST]] data. This means that the convolutional layer already makes your data representation sparser. What's more, this effect gets even stronger when [[Layers|layers]] like [[Pooling]] are applied
>    
> - [Zeiler Fergus](Zeiler Fergus.md)
>   - multiple interleaved [[Layers|layers]] of [[Conv]], non-linear [[ActivationFunctions]], local response normalizations, and max [[Pooling]]
>    
> - [Receptive Field](Receptive field.md)
>   - Not for Dense, only local connected [[Layers|layers]] like [[Conv]], [[Pooling]]

_Backlinks last generated 2022-07-26 20:33:15_
