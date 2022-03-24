# MSE
- $$L(x) = \Sigma_i ||D(E(x_i))||^2$$
- $$MSE = \frac{1}{N} \Sigma^N_{i=1}(p(x_i) - y_i)^2$$

## Backlinks
* [[MSLE]]
	* [[MSE]] log error
* [[Huber/Smooth L1/Smooth MAE]]
	* It is less sensitive to outliers than the [[MSE]] and in some cases prevents exploding #gradients
* [[Log Cosh]]
	* works like the [[MSE]], but is smoothed towards large errors (presumably caused by outliers) so that the final error score isn’t impacted thoroughly.
* [[Loss Functions]]
	* [[MSE]]

## ...