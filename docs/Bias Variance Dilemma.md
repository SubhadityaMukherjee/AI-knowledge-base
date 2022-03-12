# Bias Vs Variance
- ![[Pasted image 20220312132539.png]]
- ![[Pasted image 20220312135948.png]]
	- m is choices of PC vectors
	- as m increases, weight matrices grow by $10\cdot m$ . Aka more flexible models.
	- Increasing tail of MSEtest -> overfitting. too flexible
	- Increasing flexibility -> decrease of empirical risk
	- Inc : very low to very high -> less and less underfitting then overfitting
	- Best: min point in curve. But it is defined on test data which we do not have
- ![[Pasted image 20220312134708.png]]
- ![[Pasted image 20220312134752.png]]
- Decision function should minimize [[LossFunctions]] and yield a function with risk h. This is hopeless $$R(h) = E[L(h(X), Y)]$$
- Tune on [[Emperical Risk]] instead using [[Optimizers]] 
- $\mathcal{H}$ is hypothesis space (related to [[Fitting]]). 

## [[Tuning Model Flexibility]]