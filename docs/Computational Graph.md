---
title: Computational Graph

tags: temp 
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Computational Graph
- ![[assets/Pasted image 20220810163656.png]]
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
	- [[loss]] function can be seen as extra nodes in the end of the graph

## Backlinks
> - [[Static Graph Execution]]
>   - [[.md|Computational Graph]] is first built then is executed

_Backlinks last generated 2022-08-10 16:56:31_
