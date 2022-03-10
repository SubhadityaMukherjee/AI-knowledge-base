## Fitting
- Bayes risk
	- Minimal expected risk over set of all functions $$R_B = min_{f\in y^X} R(f)$$
	- If minimized -> Best possible function
	- Capacity of hypothesis space 
		- If low, $$\mathscr{F}  = R(f) - R_B$$ is large : Underfitting (Huge difference between best risk and current risk)
		- If high, $$\mathscr{F}  = R(f) - R_B$$ is small : Overfitting (Tiny difference between best risk and current risk)