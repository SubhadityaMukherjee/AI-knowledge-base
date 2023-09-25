---
title: Vanishing Gradient

tags: gradients  
date modified: Tuesday 7th February 2023, Tue
date created: Tuesday 7th February 2023, Tue
---

# Vanishing Gradient
```toc
```

- Deltas become smaller initially. using [[Sigmoid]] -> [[ill conditioning]] 
- $$g(x) = (1+e^{-x})^{-1}$$
- $$\nabla_{x}[g] = g(1-g) \in [0,1]$$
- Saturation and prevent [[Backprop]] 
- $$g(x) \approx 1 \rightarrow \nabla_{x}[g] \approx 0 $$
- Weight matrices are usually initialized with random values $|w_{ji}| << 1$ 
	- gradient magnitueds decay exponentially -> max eigenvalue



