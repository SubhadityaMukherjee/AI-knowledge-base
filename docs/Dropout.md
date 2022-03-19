## Dropout
- Applied to Dense layers
- Training : Randomly (Bernoulli, p = 0.5 say) set #activations to 0
- Generally p = 0.1, 0.5
- Testing: Reweight by p
	- Because after training values will increase by $$1/(1-p)$$
- Reduces co dependence between neurons
- Decreases overfitting
<<<<<<< HEAD
- Start with small rate : 20 %



## Backlinks
* [[Regularization]]
	* [[Dropout]]
* [[Noise]]
	* [[Dropout]]

## ...
=======
- Start with small rate : 20 %## Backlinks
* [[Regularization]]
	* [[Dropout]]
* [[Adding noise]]
	* [[Dropout]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
