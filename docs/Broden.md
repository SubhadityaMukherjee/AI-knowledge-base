---
title: Broden

tags: dataset explainability 
date modified: Thursday, November 24th 2022, 1:46:39 pm
date created: Thursday, November 24th 2022, 1:46:37 pm
---

# Broden
```toc
```

- Broadly and Densely Labeled Dataset
- unifies several densely labeled image data sets: ADE [43], OpenSurfaces [4], Pascal-Context [19], Pascal-Part [6], and the Describable Textures Dataset [7]
- These data sets contain examples of a broad range of objects, scenes, object parts, textures, and materials in a variety of contexts
- segmented down to the pixel level except textures and scenes which are given for full-images
- every image pixel in the data set is annotated with one of the eleven common color names according to the human perceptions classified by van de Weijer
- The concept labels in Broden are normalized and merged from their original data sets so that every class corresponds to an English word
- Labels are merged based on shared synonyms, disregarding positional distinctions such as 'left' and 'top'

## Backlinks

> - [Network Dissection Quantifying Interpretability of Deep Visual Representions](Network Dissection Quantifying Interpretability of Deep Visual Representions.md)
>   - [[Broden]]
>   - evaluates every individual convolutional unit in a CNN as a solution to a binary segmentation task to every visual concept in [[Broden]]
>   - For every input image x in the [[Broden]] dataset, the activation map $A_{k}(x)$ of every internal convolutional unit k is collected.

_Backlinks last generated 2023-01-16 19:33:15_
