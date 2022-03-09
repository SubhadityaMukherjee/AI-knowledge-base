## Ridge Regression
- $(XX')$ suffers from numerical instability when almost singular (real world data. sparse I think)
- Add a tiny term
	- $w'_{opt} = (XX' + \alpha ^2 I_{nxn})^{-1}Xy$
	- Solution to overfitting