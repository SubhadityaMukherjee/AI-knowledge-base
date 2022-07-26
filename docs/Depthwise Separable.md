---
title: Depthwise Separable
---

# Depthwise Separable
- Only transforms the input once and saves computation -> elongate it to more channels
- From C -> F channels : Use F instances of a 1x1xC filter
- ![[assets/Pasted image 20220306122226.png|im]]


































































































## Backlinks

> - [ConvNeXt](ConvNeXt.md)
>   - [[Depthwise Separable]] , which are interestingly similar to self-[[Attention]] as they work on a per-channel basis
>    
> - [Mobile Net](Mobile Net.md)
>   - [[Depthwise Separable]]
>    
> - [Xception](Xception.md)
>   - Only use [[Depthwise Separable]] convs + [[Inception]] modules
>    
> - [Receptive Field](Receptive field.md)
>   - [[Depthwise Separable]]
>    
> - [Convnd](Conv.md)
>   - [[Depthwise Separable]]

_Backlinks last generated 2022-07-26 20:33:15_
