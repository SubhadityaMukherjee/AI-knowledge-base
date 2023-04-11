---
title: Filter Wise Normalization

tags: explainability 
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Filter Wise Normalization
```toc
```

- Following up from [[Random Directions]] 
$$
d_{i,j} \leftarrow \frac{d_{i,j}}{||d_{i,j}||}||\theta_{i,j}||
$$
	- d is a random Gaussian Direction vector
	- $d_{i,j}$ is $j_{th}$ filter of the $i_{th}$ layer of the direction vector d
	- $||\cdot||$ is the [[Frobenius norm]]
- ![[images/Pasted image 20230327130027.png]]
- ![[images/Pasted image 20230327130311.png]]

## Backlinks

> - [Visualizing the Loss Landscape of Neural Nets](Visualizing the Loss Landscape of Neural Nets.md)
>   - [[Filter Wise Normalization]]

_Backlinks last generated 2023-04-11 15:00:45_
