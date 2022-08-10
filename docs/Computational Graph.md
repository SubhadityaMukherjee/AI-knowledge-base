---
title: Computational Graph

tags: temp 
date modified: Wednesday, August 10th 2022, 7:05:41 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Computational Graph
- ![](assets/Pasted%20image%2020220810163656.png)
- patterns in backward flow
	- add gate: gradient distributor
	- max gate: gradient router
	- mul gate: gradient switcher
	- branches: sum up gradients
- pros
	- intuitive interpretation of gradient
	- easily define new nodes using forward/backward pattern (i.e. only these two functions must be implemented)
	- any complex learning architecture can be composed of atomic nodes (node composition or factorization)
	- no need to compute manually complex gradients
	- [loss](loss.md) function can be seen as extra nodes in the end of the graph

## Backlinks
> - [Static Graph Execution](Static Graph Execution.md)
>   - [[Computational Graph]] is first built then is executed

_Backlinks last generated 2022-08-10 16:56:31_
