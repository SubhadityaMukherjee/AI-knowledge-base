---
title: Dilated Sliding Window Attention

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Dilated [[Sliding Window Attention]]
- Analgous to dilated CNN
- Assuming a fixed $d$ and $w$ for all [[Layers|layers]], [[Receptive field|receptive field]] is $l \times d \times w$ which can reach tens of thousands of tokens even with small values of $d$
- ![[assets/Pasted image 20220621181124.png]]

## Backlinks
> - [Global and [[Sliding Window Attention]]](Global and Sliding Window Attention.md)
>   - [[Sliding Window Attention]] and [[Dilated Sliding Window Attention]] are not always enough
>
> - [Attention](Attention.md)
>   - [[Dilated Sliding Window Attention]]
>
> - [Longformer](Longformer.md)
>   - [[Dilated Sliding Window Attention]]

_Backlinks last generated 2022-10-04 13:01:19_
