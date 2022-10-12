---
title: FaceNet
tags: architecture
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FaceNet
- [FaceNet: a Unified Embedding for Face Recognition and Clustering](https://arxiv.org/abs/1503.03832)
- mapping from face images to a compact Euclidean space where distances directly correspond to a measure of face similarity
- Optimize the [[Embedding|embedding]] itself
- FaceNet directly trains its output to be a compact 128-D [[Embedding|embedding]] using a [[Triplet Loss]] function
- Choosing which triplets to use turns out to be very important for achieving good performance
	- inspired by [[Curriculum Learning|curriculum learning]]
	- online negative exemplar mining strategy which ensures consistently increasing difficulty of triplets as the network trains
	- also explore hard-positive mining techniques which encourage spherical clusters for the embeddings of a single person
- squared [[Lp Regularization]] L2 distance, in the [[Embedding|embedding]] space directly correspond to face similarity: faces of the same person have small distances and faces of distinct people have large distances
- face verification simply involves thresholding the distance between the two embeddings; recognition becomes a [[KNN]] classification problem
- [[Labeled Faces in the Wild]]
- [[Zeiler Fergus]]
- [[Inception]]
- [[Harmonic Embedding]]

## Backlinks
> - [Triplet [[loss|Loss]]](Triplet Loss.md)
>   - Face recog [[FaceNet]]

_Backlinks last generated 2022-10-04 13:01:19_
