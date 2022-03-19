# Cross Validation

## KFold
- Repeat for m = 1..L
	- Split data into roughly equal sizes. Disjoint subsets
	- Get model with min [[Emperical Risk]]
	- Test it with validation set
	- Avg it for the folds for this value of m
- Find optimal class for that m that had min avg validation risk (aka training error)
- Compute $h_{opt}$ using the original training data

## Leave One Out
- Each D contains a single training example
<<<<<<< HEAD
- For tiny datasets



## Backlinks
* [[Tuning Model Flexibility]]
	* [[Cross Validation]]

## ...
=======
- For tiny datasets## Backlinks
* [[Tuning Model Flexibility]]
	* [[Cross Validation]]

>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
