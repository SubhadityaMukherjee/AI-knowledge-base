## Fitting
- Bayes risk
	- Minimal expected risk over set of all functions $$R_B = min_{f\in y^X} R(f)$$
	- If minimized -> Best possible function
	- Capacity of hypothesis space $\mathcal{H}$ 
	- It is essentally all possible things. In reg, all possible affine linear fns. In neural networks, all possible specific connection structure.
		- If low, $$\mathscr{F}  = R(f) - R_B$$ is large : Underfitting (Huge difference between best risk and current risk)
<<<<<<< HEAD
		- If high, $$\mathscr{F}  = R(f) - R_B$$ is small : Overfitting (Tiny difference between best risk and current risk)



## Backlinks
* [[Issues]]
	* [[Fitting]]
* [[Bias Vs Variance]]
	* $\\mathcal{H}$ is hypothesis space (related to [[Fitting]]). 

## ...
=======
		- If high, $$\mathscr{F}  = R(f) - R_B$$ is small : Overfitting (Tiny difference between best risk and current risk)## Backlinks
* [[Bias Variance Dilemma]]
	* $\\mathcal{H}$ is hypothesis space (related to [[Fitting]]). 
* [[Issues]]
	* [[Fitting]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
