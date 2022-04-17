---
title: Margin Ranking
---

# Margin Ranking
- Creates a criterion that measures the loss given inputs x1x1x1 , x2x2x2 , two 1D mini-batch Tensors, and a label 1D mini-batch tensor yyy (containing 1 or -1).
- If y=1y = 1y=1 then it assumed the first input should be ranked higher (have a larger value) than the second input, and vice-versa for y=−1y = -1y=−1 .
- take avg

$$\frac{1}{\mathrm{length}\left( y \right)} \cdot \mathrm{sum}\left( \mathrm{max}\left( 0, \left(  - y \right) \cdot x1 - x2 + margin \right) \right)$$





## Backlinks
* [[Loss Functions]]
	* [[Margin Ranking]]
