---
title: Trajectory Plotting with PCA

tags: explainability 
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Trajectory Plotting with PCA
```toc
```

- The problem: the path lies in a low-dimensional space.
- The solution: [[PCA]]
- Construct a matrix $$
M = [\theta_{0}- \theta_{n};...;\theta_{n-1}-\theta_{n}]
$$
- where,
- $\theta_{i}$ is the model params during epoch i
- n is number of epochs
- apply PCA to M and use 2 most explanatory directions
- ![[images/Pasted image 20230327130326.png]]

## Backlinks

> - [Visualizing the Loss Landscape of Neural Nets](Visualizing the Loss Landscape of Neural Nets.md)
>   - [[Trajectory Plotting with PCA]]

_Backlinks last generated 2023-04-11 15:00:45_
