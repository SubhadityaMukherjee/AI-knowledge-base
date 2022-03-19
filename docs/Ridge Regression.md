## Ridge Regression
- [[LinearRegression]]
- $$(XX')$$ suffers from numerical instability when almost singular (real world data. sparse I think)
- Add a tiny term
	- $$w'_{opt} = (XX' + \alpha ^2 I_{nxn})^{-1}XY$$
	- Solution to overfitting



## Backlinks
* [[Tuning Model Flexibility]]
	* [[Ridge Regression]]
* [[Linear Regression]]
	* [[Ridge Regression]]

## ...