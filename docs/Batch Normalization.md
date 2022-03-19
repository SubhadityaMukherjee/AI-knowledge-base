## Batch Normalization
- bias=False for Linear/Conv2D for input and True for output #tricks
- Normalizes #activations
- Input distributions change per layer -> Make sure they stay similar
- Reduces co variate shift because now the network must adapt per layer
- During testing : use stats saved during training
- Simplifies learning dynamics
	- Can use larger learning rate
	- Higher order interactions are suppressed because the mean and std are independant of the activations which makes training easier
- Cant work with small batches. Not great with RNN
- ![[Pasted image 20220306114903.png]]
- $$\mu_j \leftarrow \frac{1}{m}\Sigma_{i=1}^m x_{ij}$$
- $$\sigma^2_j \leftarrow \frac{1}{m}\Sigma^m_{i=1}(x_{ij}-\mu_j)^2$$
- $$\hat x_{ij} \leftarrow \frac{x_{ij}-\mu_j}{\sqrt{\sigma^2_j + \epsilon}}$$
<<<<<<< HEAD
- $$\hat x_{ij} \leftarrow \gamma \hat x_{ij} + \beta$$



## Backlinks
* [[Regularization]]
	* [[Batch Normalization]]

## ...
=======
- $$\hat x_{ij} \leftarrow \gamma \hat x_{ij} + \beta$$## Backlinks
* [[Regularization]]
	* [[Batch Normalization]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9