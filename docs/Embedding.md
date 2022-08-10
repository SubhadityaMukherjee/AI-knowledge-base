---
tags: temp
title: Embedding
date modified: Wednesday, August 10th 2022, 7:05:53 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Embedding
- More complex than 1 hot
- Lookup table is an example.
	- $$token\_embedding(i) = gather(W, i)$$
- Say vocabulary is (the cat walks)
	- Embedding vector v that will be learnt
	- Values like : $v_{the}$, $v_{cat}$, $v_{walks}$

