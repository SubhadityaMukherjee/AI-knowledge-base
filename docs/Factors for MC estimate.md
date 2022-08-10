---
tags: temp
title: Factors for MC Estimate
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Factors for MC Estimate
- Amount of computation required to simulate transition kernel
- Time for chain to converge to equilibrium -> no of states that must be discarded
- No of transitions needed to move from one state in the equilibrium to another that is independant
	- Redundant information
	- First value will depend to a decreasing degree on the distance from this timestep to the previous ones. Then washout (because old ones are too far away)

