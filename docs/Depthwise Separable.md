---
tags: temp
title: Depthwise Separable
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Depthwise Separable
- Only transforms the input once and saves computation -> elongate it to more channels
- From C -> F channels : Use F instances of a 1x1xC filter
- ![[assets/Pasted image 20220306122226.png|im]]

## Backlinks
> - [Receptive Field](Receptive field.md)
>   - [[Depthwise Separable]]
>
> - [Xception](Xception.md)
>   - Only use [[Depthwise Separable]] convs + [[Inception]] modules
>
> - [Mobile Net](Mobile Net.md)
>   - [[Depthwise Separable]]
>
> - [ConvNeXt](ConvNeXt.md)
>   - [[Depthwise Separable]] , which are interestingly similar to self-[[Attention]] as they work on a per-channel basis
>
> - [Convnd](Conv.md)
>   - [[Depthwise Separable]]

_Backlinks last generated 2022-10-04 13:01:19_
