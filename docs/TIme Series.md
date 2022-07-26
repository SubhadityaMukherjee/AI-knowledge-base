---
title: Time Series Prediction
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
	- [[HMM]]
	- [[Recurrent]]


































































































## Backlinks

> - [Window Based Regression](Window Based Regression.md)
>   - [[TIme Series]]
>    
> - [Autoregressive](Autoregressive.md)
>   - predict the future by past of [[TIme Series]]
>    
> - [Causal Systems](Causal Systems.md)
>   - [[TIme Series]]

_Backlinks last generated 2022-07-26 20:33:15_
