# Feature Learning

## Dictionary Learning
- Given : N unlabeled data points $$x_i \in \mathcal{R}^d$$
- To find:
	- Linear rep of these points based on set of basis vectors
		- $$x = \Sigma_i^k r_i \cdot d_i = Dr$$
		- dimension d
		- r are repr weights corresponding to basis vector d
		- D is a dict with basis vectors
		- R contains weights. Scalar
		- $$||d_i|| \leq 1$$
- [[Sparse Dictionary Learning Loss]]
- After learning, these can be used as discriminative features
	- Expensive to compute

## Methods to Learn
- Start with a random dict and rep. Update D while keeping r fixed -> find best r while keeping D fixed. Repeat until convergence. 
- Move D in a direction to minimize loss and project it back
	- [[Gradient Descent gradients]] or [[LinearRegression]]
## Backlinks
<<<<<<< HEAD
* [[Unsupervised]]
	* [[Feature Learning]]

## ...



## Backlinks
* [[Feature Learning]]
	* [[Feature Learning]]
* [[Unsupervised]]
	* [[Feature Learning]]

## ...
=======
* [[Unsupervised Learning]]
	* [[Feature Learning]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
