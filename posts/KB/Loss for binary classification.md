---
title: Loss for binary classification
toc: true
categories:
  - loss
date modified: Wednesday 28th August 2024, Wed
date created: Wednesday 28th August 2024, Wed
---

# Loss for binary classification
```toc
```
- Two classes
- Probability distribution - [Bernoulli Distribution](Bernoulli%20Distribution.md)
- Training -> Model to predict $\lambda$, but these values might not lie in [0,1] and we need it to. -> [Sigmoid](Sigmoid.md)
- [Cross Entropy](Cross%20Entropy.md)
- ![Pasted image 20240828101513](Pasted%20image%2020240828101513.png)
- This represents the probability that y = 1, and it follows that 1 − λ represents the probability that y = 0. When we perform inference, we may want a point estimate of y, so we set y = 1 if λ > 0.5 and y = 0 otherwise.
- ![Pasted image 20240828101723](Pasted%20image%2020240828101723.png)