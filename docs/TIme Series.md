---
tags: temp
title: Time Series Prediction
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Time Series Prediction
- Task:
	- discrete time, equidistant timesteps
	- Approximate teacher signal
	- Input signal : $$u(t)_{t \in \mathcal{T}}$$
	- Desired output : $$(y(t))_{t \in \mathcal{T}} = u(t+h))_{t \in \mathcal{T}}$$
	- Dynamical system state : $$x(t) \in \mathbb{R}^n$$
	- Temporal evolution governed by
		- State update map
			- Governs how $$x(t)$$ develops over time
			- $$x(t+1) = f(x(t) , u(t+1))$$
		- Observation function
			- What output can be observed when in state $$x(t)$$
			- $$y(t) = g(x(t))$$
- Short range
	- PDE , ODE
- Long range
	- [HMM](HMM)
	- [Recurrent](Recurrent.md)

